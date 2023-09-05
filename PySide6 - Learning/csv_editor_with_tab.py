import sys
import csv

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, \
    QTableWidget, QTableWidgetItem, QFileDialog, QTabWidget, QMessageBox, QHBoxLayout


class CSVEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Param Edit and Save GUI")

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.setup_tab1()
        self.setup_tab2()

    def setup_tab1(self):
        tab1 = QWidget()
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()

        self.import_button = QPushButton("Import CSV")
        self.import_button.clicked.connect(self.import_csv)
        horizontal_layout.addWidget(self.import_button, alignment=Qt.AlignHCenter)
        # layout.addWidget(self.import_button)

        self.save_button = QPushButton("Save CSV")
        self.save_button.clicked.connect(self.save_csv)
        horizontal_layout.addWidget(self.save_button, alignment=Qt.AlignHCenter)

        vertical_layout.addLayout(horizontal_layout)

        self.table = QTableWidget()
        vertical_layout.addWidget(self.table)

        tab1.setLayout(vertical_layout)
        self.tab_widget.addTab(tab1, "CSV Editor")

        self.data = []

    def setup_tab2(self):
        tab2 = QWidget()
        layout = QVBoxLayout()

        # Add your desired content for the second tab here
        # For example, a QLabel for a blank tab
        blank_label = QLabel("This is a blank tab.")
        layout.addWidget(blank_label)

        tab2.setLayout(layout)
        self.tab_widget.addTab(tab2, "Tab 2")

    def import_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", "C:", "CSV Files (*.csv)", options=options)

        if file_path:
            self.table.clearContents()
            self.data = []

            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if len(row) == 2:
                        self.data.append(row)

            self.table.setRowCount(len(self.data))
            self.table.setColumnCount(2)  # Update to 3 columns
            for row_idx, (address, value) in enumerate(self.data):  # Update row data extraction
                address_item = QTableWidgetItem(address)
                address_item.setFlags(address_item.flags() & ~Qt.ItemIsEditable)  # Make the item not editable
                value_item = QTableWidgetItem(value)
                # new_column_item = QTableWidgetItem(new_column_data)
                self.table.setItem(row_idx, 0, address_item)
                self.table.setItem(row_idx, 1, value_item)
                # self.table.setItem(row_idx, 2, new_column_item)  # Set new column item

    def save_csv(self):
        if len(self.data) == 0:
            self.show_warning_box()

        if self.data:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "C:", "CSV Files (*.csv)", options=options)

            if file_path:
                new_data = []

                for row_idx in range(self.table.rowCount()):
                    address_item = self.table.item(row_idx, 0)
                    value_item = self.table.item(row_idx, 1)
                    # new_column_item = self.table.item(row_idx, 2)

                    if address_item and value_item:
                        new_data.append([address_item.text(), value_item.text()])

                with open(file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(new_data)

    def show_warning_box(self):
        QMessageBox.warning(self, "Warning", "Please Import your file first")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVEditorApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
