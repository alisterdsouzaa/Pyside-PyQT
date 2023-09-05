import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QSpinBox, QTabWidget, \
    QScrollArea


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Windows App with PySide6")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tab_widget = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")

        self.layout.addWidget(self.tab_widget)

        self.tab1_layout = QVBoxLayout()
        self.tab1.setLayout(self.tab1_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_area_content)

        self.expand_button = QPushButton("Expand")
        self.expand_button.clicked.connect(self.expand_spinboxes)
        self.tab1_layout.addWidget(self.expand_button)

        self.spinboxes = []

        self.tab1_layout.addWidget(self.scroll_area)
        self.scroll_area_content_layout = QVBoxLayout(self.scroll_area_content)

        self.tab2_layout = QVBoxLayout()
        self.tab2.setLayout(self.tab2_layout)

        self.second_button = QPushButton("Second Button")
        self.tab2_layout.addWidget(self.second_button)

    def expand_spinboxes(self):
        if not self.spinboxes:
            for _ in range(15):
                spinbox = QSpinBox()
                self.spinboxes.append(spinbox)
                self.scroll_area_content_layout.addWidget(spinbox)
        else:
            for spinbox in self.spinboxes:
                spinbox.setParent(None)
            self.spinboxes = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
