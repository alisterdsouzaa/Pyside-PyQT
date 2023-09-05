from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QVBoxLayout, QWidget
import pyqtgraph as pg
import sys
import csv


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(True, True)
        self.layout.addWidget(self.graphWidget)

        # Add a button for importing CSV data
        self.importButton = QPushButton('Import CSV', self)
        self.layout.addWidget(self.importButton)
        self.importButton.clicked.connect(self.import_csv)

        self.selected_column = None

    def import_csv(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                  options=options)

        if filePath:
            # Read CSV data and update the plot
            data = self.read_csv(filePath)
            if data:
                self.plot_data(data)

    def read_csv(self, file_path):
        data = {'x': [], 'y': []}

        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read and store headers
            if not headers:
                return None  # No data to plot

            # Create a dialog to select the column to plot
            column, ok = pg.QtWidgets.QInputDialog.getItem(self, "Select Column", "Select a column to plot:", headers,
                                                           0, False)
            if not ok:
                return None  # User canceled the selection

            self.selected_column = column

            column_index = headers.index(column)
            for row in csv_reader:
                if len(row) > column_index:
                    x_value = row[0]
                    y_value = row[column_index]

                    try:
                        x_value = float(x_value)
                        y_value = float(y_value)
                    except ValueError:
                        continue  # Skip rows with non-numeric values

                    data['x'].append(x_value)
                    data['y'].append(y_value)

        return data

    def plot_data(self, data):
        self.graphWidget.clear()
        self.graphWidget.setBackground('w')

        # Modify the plot function to set the line color to red and increase the thickness
        self.graphWidget.plot(data['x'], data['y'], name=f'{self.selected_column}',
                                     pen=pg.mkPen(color='r', width=2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()
