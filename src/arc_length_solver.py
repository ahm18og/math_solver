# arc_length_solver.py
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

class ArcLengthSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        font = QFont()
        font.setPointSize(14)

        # Styling for labels and inputs
        self.radius_label = QLabel('Enter radius:')
        self.radius_label.setFont(font)
        layout.addWidget(self.radius_label, 0, 0)
        
        self.radius_input = QLineEdit()
        self.radius_input.setFont(font)
        layout.addWidget(self.radius_input, 0, 1)

        self.angle_label = QLabel('Enter angle (in degrees):')
        self.angle_label.setFont(font)
        layout.addWidget(self.angle_label, 1, 0)
        
        self.angle_input = QLineEdit()
        self.angle_input.setFont(font)
        layout.addWidget(self.angle_input, 1, 1)

        # Arc Length Button
        self.arc_length_button = QPushButton('Calculate Arc Length')
        self.arc_length_button.setFont(font)
        self.arc_length_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.arc_length_button.clicked.connect(self.calculate_arc_length)
        layout.addWidget(self.arc_length_button, 2, 0)

        # Area of Sector Button
        self.area_sector_button = QPushButton('Calculate Area of Sector')
        self.area_sector_button.setFont(font)
        self.area_sector_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.area_sector_button.clicked.connect(self.calculate_area_of_sector)
        layout.addWidget(self.area_sector_button, 2, 1)

        # Result label
        self.result_label = QLabel('')
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        layout.addWidget(self.result_label, 3, 0, 1, 2)

        # Back to Homepage Button
        self.back_home_button = QPushButton('Back to Homepage')
        self.back_home_button.setFont(font)
        self.back_home_button.setToolTip('Exit to the home page')
        self.back_home_button.setShortcut('Escape')
        self.back_home_button.setStyleSheet("background-color: #FF6347; color: white;")
        self.back_home_button.clicked.connect(self.showHomePage)
        layout.addWidget(self.back_home_button, 4, 1)

        self.setLayout(layout)

    def calculate_arc_length(self):
        try:
            radius = float(self.radius_input.text())
            angle = float(self.angle_input.text())
            arc_length = 2 * math.pi * radius * (angle / 360)
            self.result_label.setText(f'Arc Length: {arc_length:.2f}')
        except ValueError:
            self.result_label.setText('Please enter valid numbers.')

    def calculate_area_of_sector(self):
        try:
            radius = float(self.radius_input.text())
            angle = float(self.angle_input.text())
            area_sector = math.pi * radius ** 2 * (angle / 360)
            self.result_label.setText(f'Area: {area_sector:.2f}')
        except ValueError:
            self.result_label.setText('Please enter valid numbers.')

    def showHomePage(self):
        self.parent().setCurrentWidget(self.parent().parent().home_page)
