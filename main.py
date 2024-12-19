import sys
import random
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect
from UI import Ui_MainWindow


class CircleWidget(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        j = random.randint(1, 15)
        for i in range(j):
            diameter = random.randint(20, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)

            self.circles.append((x, y, diameter))

            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))

        for (x, y, diameter) in self.circles:
            painter.drawEllipse(QRect(x, y, diameter, diameter))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleWidget()
    ex.show()
    sys.exit(app.exec())
