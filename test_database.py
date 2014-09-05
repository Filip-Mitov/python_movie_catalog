import database
import unittest


class TestDatabasePrimaryKeysCorrection(unittest.TestCase):

    def test_add_cortege_with_primary_key_title_equal_to_none(self):
        movie_row_title_none = {
            'title': None, 'year': '',
            'genre': '', 'rating': '',
            'description': '', 'path': ''
        }

        self.assertFalse(database.add_movie(movie_row_title_none))

    def test_add_cortege_with_primary_key_year_equal_to_none(self):
        movie_row_year_none = {
            'title': '', 'year': None,
            'genre': '', 'rating': '',
            'description': '', 'path': ''
        }

        self.assertFalse(database.add_movie(movie_row_year_none))

    def test_add_cortege_with_primary_key_title_equal_to_empty_string(self):
        movie_row_title_empty_string = {
            'title': '', 'year': '',
            'genre': '', 'rating': '',
            'description': '', 'path': ''
        }

        self.assertFalse(database.add_movie(movie_row_title_empty_string))


class TestDatabaseFunctions(unittest.TestCase):

    def test_add_twice_the_same_movie_and_delete(self):
        cortege = {
            'title': 'add_function_test_title', 'year': 2014,
            'genre': '', 'rating': '',
            'description': '', 'path': ''
        }
        title, year = cortege['title'], cortege['year']
        database.delete_movie(title, year)

        self.assertTrue(database.add_movie(cortege))
        self.assertFalse(database.add_movie(cortege))
        self.assertTrue(database.delete_movie(title, year))

    def test_add_movie_with_title_equal_to_number_and_delete(self):
        cortege = {
            'title': 123456789, 'year': 2014,
            'genre': '', 'rating': '',
            'description': '', 'path': ''
        }
        title, year = cortege['title'], cortege['year']
        database.delete_movie(title, year)

        self.assertTrue(database.add_movie(cortege))
        self.assertTrue(database.delete_movie(title, year))


if __name__ == '__main__':
    unittest.main()