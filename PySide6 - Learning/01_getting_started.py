from PySide6.QtWidgets import QApplication, QWidget, QPushButton

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

window = QWidget()
window.show()


app.exec_()

