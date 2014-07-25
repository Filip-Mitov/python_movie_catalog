import sys
from PySide.QtCore import *
from PySide.QtGui import *


class FormAddMovie(QDialog):

    def __init__(self, movie_operations, parent=None):
        super(FormAddMovie, self).__init__(parent)
        self.movie_manage = movie_operations
        self.setWindowTitle('Movie catalog 2014')

        # Create widgets
        self.title = QLineEdit()
        self.year = QLineEdit()
        self.genre = QLineEdit()
        self.rating = QLineEdit()
        self.comment = QTextEdit()
        self.path = QLineEdit()
        self.button = QPushButton("add movie to catalog")

        #Create labels
        self.title_label = QLabel("title")
        self.year_label = QLabel("year")
        self.genre_label = QLabel("genre")
        self.rating_label = QLabel("rating")
        self.comment_label = QLabel("comment")
        self.path_label = QLabel("path")

        # # Create layout and add widgets and labels
        layout = QGridLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title, 0, 1)
        layout.addWidget(self.year_label)
        layout.addWidget(self.year)
        layout.addWidget(self.genre_label)
        layout.addWidget(self.genre)
        layout.addWidget(self.rating_label)
        layout.addWidget(self.rating)
        layout.addWidget(self.comment_label)
        layout.addWidget(self.comment)
        layout.addWidget(self.path_label)
        layout.addWidget(self.path)
        layout.addWidget(self.button, 6, 1)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.text)

    def text(self):
        cortege = (
            self.title.text(),
            self.year.text(),
            self.genre.text(),
            self.rating.text(),
            self.comment.toPlainText(),
            self.path.text()
        )
        if not self.movie_manage.add_movie(*cortege):
            self.warning_message("Empty title or year! Enter again.")
        else:
            self.done(True)

    def warning_message(self, message):
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitle("Warning!")
        msgBox.exec_()
