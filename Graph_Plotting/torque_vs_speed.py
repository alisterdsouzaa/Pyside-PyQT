import sys
import pandas as pd
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog


# Step 2: Read the CSV file into a pandas DataFrame
def read_csv_file():
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(None, "Open CSV File", "", "CSV Files (*.csv)")
    if not file_path:
        return None
    return pd.read_csv(file_path)


# Step 3: Create a PyQtGraph plot widget
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)

        self.load_button = QPushButton("Load CSV")
        self.load_button.clicked.connect(self.load_csv_and_plot)
        self.layout.addWidget(self.load_button)

    # Step 4: Plot the data on the graph widget
    def plot_data(self, df):
        if df is not None:
            self.plot_widget.clear()
            x_column = df.columns[0]  # Replace with your X-axis column name
            y_column = df.columns[1]  # Replace with your Y-axis column name
            self.plot_widget.plot(df[x_column], df[y_column], pen=None, symbol='o', symbolPen=None, symbolSize=5)

    def load_csv_and_plot(self):
        df = read_csv_file()
        self.plot_data(df)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle("CSV Data Plotter with PyQtGraph")
    window.show()
    sys.exit(app.exec())
