import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel


class TabbedApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabbed GUI Application")
        self.setGeometry(100, 100, 800, 600)

        # Create a tab widget
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Create tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        # Add content to tabs
        self.add_content_to_tab(self.tab1, "This is Tab 1")
        self.add_content_to_tab(self.tab2, "This is Tab 2")
        self.add_content_to_tab(self.tab3, "This is Tab 3")

    def add_content_to_tab(self, tab, content):
        layout = QVBoxLayout()
        label = QLabel(content)
        layout.addWidget(label)
        tab.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use the Fusion style

    window = TabbedApplication() #create obj
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
