import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

STEP = 30


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.x = 0
        self.y = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Управление НЛО')

        ## Изображение
        self.pixmap = QPixmap('ufo.png').scaled(100, 100)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.resize(100, 100)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_Up:
            self.y -= STEP
        elif a0.key() == Qt.Key_Down:
            self.y += STEP
        elif a0.key() == Qt.Key_Left:
            self.x -= STEP
        elif a0.key() == Qt.Key_Right:
            self.x += STEP

        self.x %= self.width()
        self.y %= self.height()

        self.image.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
