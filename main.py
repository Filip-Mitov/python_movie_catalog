from gui import *
from database import *


# movie_database = Database('movie_catalog.db')
# movie_operations = Movie(movie_database)
# movie_operations.all_movies()

# form = Form(movie_operations)

def main():
    movie_database = Database('movie_catalog.db')
    movie_operations = Movie(movie_database)

    # movie_operations.all_movies()

    app = QApplication(sys.argv)
    form = FormAddMovie(movie_operations)

    wid = QWidget()

    button = QPushButton('Add movie to catalog')
    button.clicked.connect(form.exec_)


    label = QLabel('picture')
    picture = QPixmap('Salt.jpg').scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    label.setPixmap(picture)
    label.setAlignment(Qt.AlignCenter)

    lab = QLabel('pic')
    pic = QPixmap('Flypaper.jpg').scaled(lab.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    lab.setPixmap(pic)
    lab.setAlignment(Qt.AlignCenter)

    lab2 = QLabel('pic')
    pic2 = QPixmap('The Hangover.jpg').scaled(wid.size(), Qt.KeepAspectRatio,Qt.SmoothTransformation)
    lab2.setPixmap(pic2)
    lab2.setAlignment(Qt.AlignCenter)


    grid = QGridLayout()
    grid.addWidget(button,0,0)
    grid.addWidget(QLabel(''),0,1)
    grid.addWidget(QLabel(''),0,2)

    grid.addWidget(label,1,0)
    grid.addWidget(lab,1,1)
    grid.addWidget(lab2,1,2)

    wid.setWindowTitle('Movie catalog 2014')
    wid.setLayout(grid)
    wid.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()