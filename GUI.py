from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QComboBox, QVBoxLayout, QLabel, QPushButton, QGroupBox
from PyQt6.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PFR Scraper")
        self.setMinimumSize(300, 500)

        team_names = ("Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", "Carolina Panthers",
                     "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", "Dallas Cowboys", "Denver Broncos",
                     "Detroit Lions", "Green Bay Packers", "Houston Texans", "Indianapolis Colts",
                     "Jacksonville Jaguars",
                     "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams",
                     "Miami Dolphins",
                     "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
                     "New York Jets",
                     "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks",
                     "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders")

        file_menu_item = self.menuBar().addMenu("&File")
        edit_menu_item = self.menuBar().addMenu("&Edit")
        help_menu_item = self.menuBar().addMenu("&Help")

        # Message above combo box
        self.team_label = QLabel("Select a team:", self)
        self.team_label.setFixedHeight(15)

        # Combo box of team names
        self.team_name = QComboBox()
        self.team_name.addItems(team_names)
        self.team_name.setFixedHeight(20)

        # Submit button
        self.button = QPushButton("Submit")
        self.button.setFixedHeight(20)
        self.button.clicked.connect(self.submit_selection)

        # Team logo field
        self.team_logo = QIcon()

        # Status text field
        # TODO

        # Group UI elements
        main_group = QGroupBox()

        # Set layout
        layout = QVBoxLayout()  # Aligns UI elements vertically
        layout.addWidget(self.team_label)
        layout.addWidget(self.team_name)
        layout.addWidget(self.button)

        widget = QWidget()  # Set dummy widget to be used in setCentralWidget
        widget.setLayout(layout)
        widget.setContentsMargins(0, 200, 0, 300)
        self.setCentralWidget(widget)
        # self.setLayout(layout)

    def submit_selection(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
