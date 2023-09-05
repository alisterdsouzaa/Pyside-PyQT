import sys
import csv

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, \
    QTableWidgetItem, QFileDialog

file_path = ""
file_path_save = ""

class CSVEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Editor")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.import_button = QPushButton("Import CSV")
        self.import_button.clicked.connect(self.import_csv)
        self.layout.addWidget(self.import_button)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.save_button = QPushButton("Save CSV")
        self.save_button.clicked.connect(self.save_csv)
        self.layout.addWidget(self.save_button)

        self.data = []

    def import_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", "D:", "CSV Files (*.csv)", options=options)
        print(f"imported file path -->" is {file_path})

        if file_path:
            self.table.clearContents()
            self.data = []

            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if len(row) == 3:
                        self.data.append(row)

            self.table.setRowCount(len(self.data))
            self.table.setColumnCount(3)

            for row_idx, (address, value, new_column_data) in enumerate(self.data):
                address_item = QTableWidgetItem(address)
                address_item.setFlags(address_item.flags() & ~Qt.ItemIsEditable)  # Make the item not editable
                value_item = QTableWidgetItem(value)
                new_column_item = QTableWidgetItem(new_column_data)
                new_column_item.setFlags(new_column_item.flags() & ~Qt.ItemIsEditable)  # Make the item not editable
                self.table.setItem(row_idx, 0, address_item)
                self.table.setItem(row_idx, 1, value_item)
                self.table.setItem(row_idx, 2, new_column_item)

    def save_csv(self):
        if self.data:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            global file_path_save
            file_path_save, _ = QFileDialog.getSaveFileName(self, "Save CSV", "D:", "CSV Files (*.csv)", options=options)

            if file_path_save:
                new_data = []

                for row_idx in range(self.table.rowCount()):
                    address_item = self.table.item(row_idx, 0)
                    value_item = self.table.item(row_idx, 1)
                    new_column_item = self.table.item(row_idx, 2)

                    if address_item and value_item:
                        new_data.append([address_item.text(), value_item.text(), new_column_item.text()])

                with open(file_path_save, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(new_data)

                print(f"Saved file path is  {file_path_save}")

    # Initialize an empty list to store the values from the first column
    first_column_values = []
    def addIndex_newTab(self):
        # Open the CSV file for reading
        global first_column_values
        with open('../Pyside6 - QStack/v3.0.0 - Akash_m2 (1) (2).csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Iterate over each row in the CSV file
            for row in csv_reader:
                first_column_values.append(row[0])

        # Print the list of values from the first column
        # print(first_column_values)
        first_column_values = first_column_values[1:]
        print(first_column_values)

        int_addresses = [int(hex_address, 16) >> 8 for hex_address in first_column_values]
        print(int_addresses)
        # shifted_hex_addresses = [hex(address) for address in int_addresses]
        # print(shifted_hex_addresses)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVEditorApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
