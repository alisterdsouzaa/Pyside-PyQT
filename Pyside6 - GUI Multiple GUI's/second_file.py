import sys
import csv
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from save_button_integration import *

count_list = []
zeroth_column_values = []
first_column_values = []
second_column_values = []
i = -1  # Values in Description
j = -1  # Values in Spin box ( Decimal values )


class listLayout(QMainWindow):
    def __init__(self):
        super(listLayout, self).__init__()

        self.run()
        # self.createStackLayout()

    def run(self):

        self.load_and_count_csv()
        self.leftlist = QListWidget()
        self.leftlist.setMaximumWidth(300)

        self.item_names = ['MotorParam',
                           'Password',
                           'Throttle Limit Look Up Table',
                           'Hardware',
                           'Motor Manger2 Params',
                           'Battery',
                           'UserFeatureParam',
                           'Throttle Map gain Param',
                           'Motor Control LUT1',
                           'Motor Control LUT2',
                           'Field Weakening LUT'
                           ]  # Add more item names if needed

        self.stack_layouts = {}  # Dictionary to store stack layouts

        for item_name in self.item_names:
            stack_layout = QWidget()
            self.createStackLayout(stack_layout, item_name)
            self.stack_layouts[item_name] = stack_layout
            self.leftlist.addItem(item_name)

        self.Stack = QStackedWidget(self)
        for item_name, stack_layout in self.stack_layouts.items():
            scroll_area = QScrollArea()  # Create a QScrollArea
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(stack_layout)
            self.Stack.addWidget(scroll_area)

        self.leftlist.currentRowChanged.connect(self.display)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        # self.setGeometry(100, 100, 800, 600)
        return hbox

    def load_and_count_csv(self):
        global count_list
        global second_column_values
        global zeroth_column_values
        global first_column_values

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", "D:", "CSV Files (*.csv)", options=options)

        if file_path:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    zeroth_column_values.append(row[0])
                    first_column_values.append(row[1])
                    second_column_values.append(row[2])

            zeroth_column_values = zeroth_column_values[1:]
            first_column_values = first_column_values[1:]
            second_column_values = second_column_values[1:]

            int_addresses = [int(hex_address, 16) >> 8 for hex_address in zeroth_column_values]

            number_counts = {}

            for num in int_addresses:
                if num in number_counts:
                    number_counts[num] += 1
                else:
                    number_counts[num] = 1

            count_list = [number_counts.get(i, 0) for i in range(11)]
            # print(int_addresses)
            # print(count_list)
            print(zeroth_column_values)
            print(first_column_values)
            print(second_column_values)

    def createStackLayout(self, stack_layout, item_name):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(item_name))

        # print("Item name:", item_name)
        # print("Count list:", count_list)

        global i
        global j
        for _ in range(count_list[self.item_names.index(item_name)]):
            row_layout = QHBoxLayout()
            row_layout.setAlignment(Qt.AlignTop)

            label1 = QLabel(zeroth_column_values[i])
            label2 = QLabel(second_column_values[i])

            label1.setAlignment(Qt.AlignVCenter)
            label2.setAlignment(Qt.AlignVCenter)

            spin_box = QSpinBox()
            spin_box.setMinimum(-100000000)
            spin_box.setMaximum(100000000)
            spin_box.setValue(int(first_column_values[i]))  # Convert value to integer

            row_layout.addWidget(label1)
            row_layout.addWidget(label2)
            row_layout.addWidget(spin_box)

            layout.addLayout(row_layout)
            i += 1
            j += 1

        stack_layout.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

    def save_csv(self):
        pass
