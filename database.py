import os

from sqlalchemy import create_engine, Column, Integer, String, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///movie_catalog.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Movie(Base):
    __tablename__ = 'movies'

    title = Column(String, primary_key=True)
    year = Column(Integer, primary_key=True)
    genre = Column(String)
    rating = Column(String)
    description = Column(String)
    path = Column(String)

    def __repr__(self):
        return '{} {} {} {} {} {}'.format(self.title,self.year,self.genre,self.rating,self.description,self.path)


Base.metadata.create_all(engine)

def add_movie(cortege):
    session = Session()
    try:
        if cortege['title'] == '':
            cortege['title'] = None
        user = Movie(**cortege)
        session.add(user)
        session.commit()
        session.close()
        return True
    except:
        session.close()
        return False

def delete_movie(title, year):
    session = Session()
    try:
        movie = session.query(Movie).filter(and_(Movie.title==title, Movie.year ==year)).one()
        session.delete(movie)
        session.commit()
        session.close()
        return True
    except:
        print('Delete movie error from form view movie')
        session.close()
        return False

def edit_movie(title, year, new_title, new_year, genre, rating, description, path):
    session = Session()
    try:
        movie = session.query(Movie).filter(and_(Movie.title==title, Movie.year ==year)).one()
        movie.title = new_title
        movie.year = new_year
        movie.genre = genre
        movie.rating = rating
        movie.description = description
        movie.path = path
        session.commit()
        session.close()
        return True
    except:
        print('Edit movie error')
        session.close()
        return False

def all_movies():
    session = Session()
    movies = session.query(*Movie.__table__.columns).all()
    session.close()
    return movies

def path_check():
    session = Session()
    for movie in session.query(Movie).all():
        if not os.path.exists(movie.path):
            session.delete(movie)
    session.commit()
    session.close()

def printer():
    session = Session()
    for row in session.query(Movie):
        print(row)
    session.close()

# printer()