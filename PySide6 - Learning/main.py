import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget


# Create a subclass of QMainWindow to define your custom window
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and initial geometry
        self.setWindowTitle("Button and Input Example")
        self.setGeometry(100, 100, 400, 300)

        # Create a vertical layout to hold the widgets
        layout = QVBoxLayout()

        # Create a QPushButton and connect its clicked signal to a slot
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        # Create a QLineEdit widget for input
        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        # Create a central widget and set the layout to it
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # Slot function to be called when the button is clicked
    def on_button_clicked(self):
        input_text = self.input_field.text()
        print("Button Clicked!")
        print("Input Text:", input_text)


if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create an instance of your custom window
    window = MyWindow()

    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
