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
        return "('{}', '{}', '{}','{}','{}','{}')".format(self.title,self.year,self.genre,self.rating,self.description,self.path)


Base.metadata.create_all(engine)

def add_movie(cortege):
    session = Session()
    try:
        if cortege['title'] == '':
            cortege['title'] = None
        user = Movie(**cortege)
        session.add(user)
        session.commit()
        return True
    except:
        return False

def delete_movie(title, year):
    session = Session()
    try:
        movie = session.query(Movie).get((title, year))
        session.delete(movie)
        session.commit()
        return True
    except:
        return False

def edit_movie(title, year, cortege):
    session = Session()
    try:
        movie = session.query(Movie).get((title, year))
        movie.title = cortege[0]
        movie.year = cortege[1]
        movie.genre = cortege[2]
        movie.rating = cortege[3]
        movie.description = cortege[4]
        movie.path = cortege[5]
        session.commit()
        return True
    except:
        return False

def path_check():
    session = Session()
    for movie in session.query(Movie).all():
        if not os.path.exists(movie.path):
            session.delete(movie)
    session.commit()
    session.close()

def all_movies():
    session = Session()
    movies = session.query(*Movie.__table__.columns).all()
    session.close()
    return movies

def selected_movies(value):
    session = Session()
    if value == '':
        return session.query(*Movie.__table__.columns).all()
    search_movies = []
    movies = session.query(*Movie.__table__.columns).all()
    for movie in movies:
        if not ''.join(str(movie)).lower().find(value.lower()) == -1:
            search_movies.append(movie)

    session.close()
    return search_movies