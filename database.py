import sqlite3


class Database(object):

    def __init__(self, file):
        self.db = sqlite3.connect(file)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()
        self.c.executescript('''
            create table IF NOT EXISTS Movie(
                title text not NULL,
                year integer not NULL,
                genre text,
                rating integer,
                comment text,
                path text,
                primary key(title, year)
            );
        ''')

    def __del__(self):
        self.db.commit()


class Movie(object):

    def __init__(self, database):
        self.db = database

    def search_movie(self, title, year):
        self.db.c.execute("""
            SELECT *
            FROM Movie
            WHERE title == ? and year == ?
            """, (title, year)
        )
        return self.db.c.fetchone()

    def add_movie(self, *cortege):
        if len(cortege[0]) == 0 and len(cortege[1]) == 0:
            return False
        if not self.search_movie(cortege[0], cortege[1]):
            self.db.c.execute('insert into Movie values(?,?,?,?,?,?)',cortege)
            return True

    def del_movie(self, title, year):
        self.db.c.execute("""
            DELETE
            FROM Movie
            WHERE title == ? and year == ?
            """, (title, year)
        )

    def edit_movie(self, title, year, *cortege):
        row = self.search_movie(title, year)
        if not row is None:
            self.del_movie(title, year)
            self.add_movie(*cortege)

    def all_movies(self):
        for cortege in self.db.c.execute('SELECT * FROM Movie'):
            print(*cortege)

# movie_operations.all_movies()
# movie_operations.add_movie('Limitless', 2012, None,None,None,None)
# movie_operations.del_movie('Up', 2012)
# movie_operations.edit_movie('Up', 2015, 'Up', 2016)


