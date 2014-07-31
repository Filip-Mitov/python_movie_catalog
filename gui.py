import sys
import os

from PySide.QtCore import *
from PySide.QtGui import *

import database


pixmap_formats = [
    '.bmp', '.gif', '.ico', '.jpeg', '.jpg',
    '.mng', '.pbm', '.pgm', '.png', '.ppm',
    '.tga', '.tif', '.tiff', '.xbm', '.xpm'
]

movie_genres = [
    "Action", "Adventure", "Animation", "Biography", "Comedy",
    "Crime", "Documentary", "Drama", "Family", "Fantasy",
    "History", "Horror", "Music", "Musical", "Mystery",
    "Romance", "Sci-Fi", "Thriller", "Western", "War"
]

movie_rating = [
    '','Awesome!', 'Very good..',
    'Average', 'Very bad..', 'Yuck!'
]


class FormAddMovie(QDialog):

    def __init__(self, parent=None):
        super(FormAddMovie, self).__init__(parent)

        self.title = QLineEdit()
        self.title_label = QLabel("Title")
        self.title_label.setAlignment(Qt.AlignRight)

        self.year = QComboBox()
        self.year.addItems([str(year) for year in range(1970, 2021)])
        self.year.setCurrentIndex(44) # Default year is 2014
        self.year_label = QLabel("Year")
        self.year_label.setAlignment(Qt.AlignRight)

        self.genre = QListWidget()
        self.genre.addItems(movie_genres)
        self.genre.setSelectionMode(QAbstractItemView.MultiSelection)
        self.genre_label = QLabel("Genre")
        self.genre_label.setAlignment(Qt.AlignRight)

        self.rating = QComboBox()
        self.rating.addItems(movie_rating)
        self.rating_label = QLabel("Rating")
        self.rating_label.setAlignment(Qt.AlignRight)

        self.description = QTextEdit()
        self.description_label = QLabel("Description")
        self.description_label.setAlignment(Qt.AlignRight)

        self.path = QPushButton("select dir")
        self.path.clicked.connect(self.choose_dir)
        self.path_display = QLabel()
        self.picture_display = QLabel()

        self.button = QPushButton("Add movie to catalog")
        self.button.clicked.connect(self.create_cortege)

        layout = QGridLayout()
        layout.addWidget(self.title_label, 0, 0)
        layout.addWidget(self.title, 0, 1)
        layout.addWidget(self.year_label, 1, 0)
        layout.addWidget(self.year, 1, 1)
        layout.addWidget(self.genre_label, 2, 0)
        layout.addWidget(self.genre, 2, 1)
        layout.addWidget(self.rating_label, 3, 0)
        layout.addWidget(self.rating, 3, 1)
        layout.addWidget(self.description_label, 4, 0)
        layout.addWidget(self.description, 4, 1)
        layout.addWidget(self.path, 5, 0)
        layout.addWidget(self.path_display,5 ,1)
        layout.addWidget(QLabel(), 6, 0)
        layout.addWidget(self.button, 6, 1)
        layout.addWidget(self.picture_display,0,2,7,2)

        self.setWindowTitle('Form add movie')
        self.setLayout(layout)

    def create_cortege(self):
        movie_row = {
            'title': self.title.text(),
            'year': int(self.year.currentText()),
            'genre': '/'.join([item.text() for item in self.genre.selectedItems()]),
            'rating': self.rating.currentText(),
            'description': self.description.toPlainText(),
            'path': self.path_display.text()
        }
        if not database.add_movie(movie_row):
            self.warning_message("Movie already exist!")
        else:
            self.done(True)
            self.closeEvent(QCloseEvent)

    def closeEvent(self, event):
        self.title.clear()
        self.year.setCurrentIndex(44)
        self.genre.clearSelection()
        self.rating.setCurrentIndex(0)
        self.description.clear()
        self.path_display.clear()
        self.picture_display.clear()

    def warning_message(self, message):
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitle("Warning!")
        msgBox.exec_()

    def choose_dir(self):
        dialog = QFileDialog(self, 'Browse movie directory')
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        if dialog.exec_():
            self.path_display.setText(*dialog.selectedFiles())
            self.set_picture_display()

    def set_picture_display(self):
        for f in os.listdir(self.path_display.text()):
            if os.path.splitext(f)[1].lower() in pixmap_formats:
                poster_path = os.path.join(self.path_display.text(), f)
                poster = QPixmap(poster_path).scaled(
                    self.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                self.picture_display.setPixmap(poster)
                break


class FormEditMovie(QDialog):

    def __init__(self, parent=None):
        super(FormEditMovie, self).__init__(parent)

        self.title = QLineEdit()
        self.title_label = QLabel("Title")
        self.title_label.setAlignment(Qt.AlignRight)

        self.year = QComboBox()
        self.year.addItems([str(year) for year in range(1970, 2021)])
        self.year_label = QLabel("Year")
        self.year_label.setAlignment(Qt.AlignRight)

        self.genre = QListWidget()
        self.genre.addItems(movie_genres)
        self.genre.setSelectionMode(QAbstractItemView.MultiSelection)
        self.genre_label = QLabel("Genre")
        self.genre_label.setAlignment(Qt.AlignRight)

        self.rating = QComboBox()
        self.rating.addItems(movie_rating)
        self.rating_label = QLabel("Rating")
        self.rating_label.setAlignment(Qt.AlignRight)

        self.description = QTextEdit()
        self.description_label = QLabel("Description")
        self.description_label.setAlignment(Qt.AlignRight)

        self.path = QPushButton("select dir")
        self.path.clicked.connect(self.choose_dir)
        self.path_display = QLabel()

        self.button = QPushButton("Edit movie in catalog")
        self.button.clicked.connect(self.edit_cortege)

        self.layout = QGridLayout()
        self.layout.addWidget(self.title_label, 0, 0)
        self.layout.addWidget(self.title, 0, 1)
        self.layout.addWidget(self.year_label, 1, 0)
        self.layout.addWidget(self.year, 1, 1)
        self.layout.addWidget(self.genre_label, 2, 0)
        self.layout.addWidget(self.genre, 2, 1)
        self.layout.addWidget(self.rating_label, 3, 0)
        self.layout.addWidget(self.rating, 3, 1)
        self.layout.addWidget(self.description_label, 4, 0)
        self.layout.addWidget(self.description, 4, 1)
        self.layout.addWidget(self.path, 5, 0)
        self.layout.addWidget(self.path_display,5 ,1)
        self.layout.addWidget(QLabel(), 6, 0)
        self.layout.addWidget(self.button, 6, 1)

        self.setWindowTitle('Form edit movie')
        self.setLayout(self.layout)

    def edit_cortege(self):
        movie_row = self.get_values()
        if database.edit_movie(self.cortege[0], self.cortege[1], *movie_row):
            self.close()

    def get_values(self):
        movie_row = (
            self.title.text(),
            int(self.year.currentText()),
            '/'.join([item.text() for item in self.genre.selectedItems()]),
            self.rating.currentText(),
            self.description.toPlainText(),
            self.path_display.text()
        )
        return movie_row

    def set_values(self, movie):
        self.cortege = movie
        self.title.setText(movie[0])
        self.year.setCurrentIndex(self.year.findText(str(movie[1])))

        selected_genre = movie[2].split('/')
        for i in range(0,self.genre.count()):
            if self.genre.item(i).text() in selected_genre:
                self.genre.item(i).setSelected(True)

        self.rating.setCurrentIndex(self.rating.findText(movie[3]))
        self.description.setText(movie[4])
        self.path_display.setText(movie[5])

    def choose_dir(self):
        dialog = QFileDialog(self, 'Browse movie directory')
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        if dialog.exec_():
            self.path_display.setText(*dialog.selectedFiles())


class FormViewMovie(QWidget):

    def __init__(self, parent=None):
        super(FormViewMovie, self).__init__(parent)
        self.edit = FormEditMovie()

        self.font_keys = QFont()
        self.font_keys.setBold(True)
        self.font_keys.setPointSize(12)

        self.font_values = QFont()
        self.font_values.setPointSize(10)

        self.title = QLineEdit()
        self.title.setReadOnly(True)
        self.title.setFont(self.font_values)
        self.title_label = QLabel("Title")
        self.title_label.setFont(self.font_keys)
        self.title_label.setAlignment(Qt.AlignRight)

        self.year = QLineEdit()
        self.year.setReadOnly(True)
        self.year.setFont(self.font_values)
        self.year_label = QLabel("Year")
        self.year_label.setFont(self.font_keys)
        self.year_label.setAlignment(Qt.AlignRight)

        self.genre = QLineEdit()
        self.genre.setReadOnly(True)
        self.genre.setFont(self.font_values)
        self.genre_label = QLabel("Genre")
        self.genre_label.setFont(self.font_keys)
        self.genre_label.setAlignment(Qt.AlignRight)

        self.rating = QLineEdit()
        self.rating.setReadOnly(True)
        self.rating.setFont(self.font_values)
        self.rating_label = QLabel("Rating")
        self.rating_label.setFont(self.font_keys)
        self.rating_label.setAlignment(Qt.AlignRight)

        self.description = QTextEdit()
        self.description.setReadOnly(True)
        self.description.setFont(self.font_values)
        self.description_label = QLabel("Description")
        self.description_label.setFont(self.font_keys)
        self.description_label.setAlignment(Qt.AlignRight)

        self.path = QLabel()
        self.path_label = QLabel('Movie directory')
        self.path_label.setFont(self.font_keys)
        self.path_label.setAlignment(Qt.AlignRight)

        self.edit_button = QPushButton('Edit movie')
        self.edit_button.clicked.connect(self.edit_cortege)

        self.button = QPushButton('Delete movie from catalog')
        self.button.clicked.connect(self.delete_cortege)

        self.layout = QGridLayout()
        self.layout.addWidget(self.title_label, 0, 0)
        self.layout.addWidget(self.title, 0, 1)
        self.layout.addWidget(self.year_label, 1, 0)
        self.layout.addWidget(self.year, 1, 1)
        self.layout.addWidget(self.genre_label, 2, 0)
        self.layout.addWidget(self.genre, 2, 1)
        self.layout.addWidget(self.rating_label, 3, 0)
        self.layout.addWidget(self.rating, 3, 1)
        self.layout.addWidget(self.description_label, 4, 0)
        self.layout.addWidget(self.description, 4, 1)
        self.layout.addWidget(self.path_label, 5, 0)
        self.layout.addWidget(self.path, 5 ,1)
        self.layout.addWidget(self.edit_button, 6, 0)
        self.layout.addWidget(self.button, 6, 1)

        self.setWindowTitle('Form view movie')
        self.setLayout(self.layout)

    def edit_cortege(self):
        self.set_values(self.edit_dialog())

    def edit_dialog(self):
        self.edit.set_values(self.cortege)
        self.edit.exec_()
        return self.edit.get_values()

    def delete_cortege(self):
        if database.delete_movie(self.title.text(), self.year.text()):
            self.picture_button.clear()
            QWidget.disconnect(self.picture_button, SIGNAL('clicked()'), self.show)
            self.close()
        else:
            pass

    def set_values(self, movie):
        self.cortege = movie
        self.title.setText(movie[0])
        self.year.setText(str(movie[1]))
        self.genre.setText(movie[2])
        self.rating.setText(movie[3])
        self.description.setText(movie[4])
        self.path.setText(movie[5])

    def view_info_button(self):
        self.picture_button = ClicableQLabel()
        self.picture_button.setAlignment(Qt.AlignCenter)
        self.movie_poster = self.poster_image(self.title.text(), self.path.text())
        self.picture_button.setPixmap(self.movie_poster)
        QWidget.connect(self.picture_button, SIGNAL('clicked()'), self.show)

    def poster_image(self, title, path):
        for one_file in os.listdir(path):
            if os.path.splitext(one_file)[1].lower() in pixmap_formats:
                poster_path = os.path.join(path, one_file)
                poster = QPixmap(poster_path).scaled(
                    self.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                return poster
        return self.blank_poster_with_text(title)

    def blank_poster_with_text(self, title):
        width, height = 320, 480
        text_poster = QPixmap(QSize(width,height))
        text_poster.fill(Qt.darkGray)
        canvas = QPainter(text_poster)
        canvas.setPen(Qt.white)
        font = QFont()
        font.setPixelSize(20)
        canvas.setFont(font)
        canvas.drawText(QRectF(0, 0, width, height), Qt.AlignCenter, title)
        return text_poster


class ClicableQLabel(QLabel):

    def __init(self, parent):
        QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('clicked()'))


class MainWindow(QWidget):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.form_add_movie = FormAddMovie()
        self.catalog_view_forms = []
        self.reload = False

        self.button = QPushButton('Add movie to catalog')
        self.button.clicked.connect(self.add_movie_and_update)

        self.scroll_area = self.picture_slideshow()

        self.grid = QGridLayout()
        self.grid.addWidget(self.button,0,0)
        self.grid.addWidget(self.scroll_area,1,0,1,3)

        self.setWindowTitle('Movie catalog 2014')
        self.setLayout(self.grid)
        self.show()

    def picture_slideshow(self):
        scroll_area = QScrollArea()
        scroll_area.setBackgroundRole(QPalette.Dark)
        scroll_widget = QWidget()
        scroll_layout = QGridLayout()
        scroll_layout.setDefaultPositioning(4, Qt.Horizontal)

        database.path_check()
        for record in database.all_movies():
            movie_view_form = FormViewMovie()
            movie_view_form.set_values(record)
            self.catalog_view_forms.append(movie_view_form)
            movie_view_form.view_info_button()
            scroll_layout.addWidget(movie_view_form.picture_button)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        return scroll_area

    def add_movie_and_update(self):
        self.form_add_movie.exec_()
        self.scroll_area = self.picture_slideshow()
        self.grid.addWidget(self.scroll_area,1,0,1,3)