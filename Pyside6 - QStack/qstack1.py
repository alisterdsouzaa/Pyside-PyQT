import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

count_of_buttons = [26, 3, 16]


class stackedExample(QWidget):

    def __init__(self):
        super(stackedExample, self).__init__()
        self.leftlist = QListWidget()

        self.item_names = ['MotorParam', 'Trottel', 'MotorMisc']  # Add more item names if needed

        self.stack_layouts = {}  # Dictionary to store stack layouts

        for item_name in self.item_names:
            stack_layout = QWidget()
            self.createStackLayout(stack_layout, item_name)
            self.stack_layouts[item_name] = stack_layout
            self.leftlist.addItem(item_name)

        self.Stack = QStackedWidget(self)
        for item_name, stack_layout in self.stack_layouts.items():
            self.Stack.addWidget(stack_layout)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('StackedWidget demo')
        self.show()

    def createStackLayout(self, stack_layout, item_name):
        global count_of_buttons
        layout = QVBoxLayout()
        layout.addWidget(QLabel(item_name))

        for _ in range(count_of_buttons[self.item_names.index(item_name)]):
            row_layout = QHBoxLayout()
            row_layout.setAlignment(Qt.AlignTop)
            row_layout.addWidget(QLabel("Field"))
            row_layout.addWidget(QSpinBox())
            layout.addLayout(row_layout)

        stack_layout.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
