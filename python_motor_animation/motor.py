import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class SpinningMotorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(100)  # Adjust the interval for the animation

    def paintEvent(self, event):
        pixmap = QPixmap("motor_image.png")  # Replace with the path to your motor image
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.angle)
        painter.drawPixmap(-pixmap.width() / 2, -pixmap.height() / 2, pixmap)

    def update_angle(self):
        self.angle += 10
        self.angle %= 360
        self.update()


class MotorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spinning Motor App")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        layout = QVBoxLayout()

        motor_widget = SpinningMotorWidget()
        layout.addWidget(motor_widget)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MotorApp()
    window.show()
    sys.exit(app.exec())
