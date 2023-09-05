import sys
import csv
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

count_list = []
second_column_values = []


class stackedExample(QWidget):

    def __init__(self):
        super(stackedExample, self).__init__()
        self.leftlist = QListWidget()

        self.item_names = ['MotorParam', 'Password', 'Throttle Limit Look Up Table', 'Hardware',
                           'Motor Manger2 Params', 'Battery', 'UserFeatureParam', 'Throttle Map gain Param',
                           'Motor Control LUT1', 'Motor Control LUT2',
                           'Field Weakening LUT']  # Add more item names if needed

        self.stack_layouts = {}  # Dictionary to store stack layouts

        self.load_and_count_csv()

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

    def load_and_count_csv(self):
        global count_list
        global second_column_values
        first_column_values = []
        second_column_values = []

        with open('v3.0.0 - Akash_m2 (1) (2).csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                first_column_values.append(row[0])
                second_column_values.append(row[2])

        first_column_values = first_column_values[1:]
        second_column_values = second_column_values[1:]

        int_addresses = [int(hex_address, 16) >> 8 for hex_address in first_column_values]

        number_counts = {}

        for num in int_addresses:
            if num in number_counts:
                number_counts[num] += 1
            else:
                number_counts[num] = 1

            count_list = [number_counts.get(i, 0) for i in range(11)]

    def createStackLayout(self, stack_layout, item_name):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(item_name))

        # Iterate through the second_column_values
        for value, count in zip(second_column_values, count_list):
            if count > 0:
                row_layout = QHBoxLayout()
                row_layout.setAlignment(Qt.AlignTop)

                # Convert 'value' to an integer before setting it to QSpinBox
                spin_box = QSpinBox()
                spin_box.setValue((value))

                row_layout.addWidget(QLabel(value))
                row_layout.addWidget(spin_box)
                layout.addLayout(row_layout)
                count -= 1

        stack_layout.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
