# rectangular_solver.py
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class RectangularSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        font = QFont()
        font.setPointSize(14)

        self.length_label = QLabel('Enter length:')
        self.length_label.setFont(font)
        layout.addWidget(self.length_label, 0, 0)
        
        self.length_line = QLineEdit()
        self.length_line.setFont(font)
        layout.addWidget(self.length_line, 0, 1)

        self.width_label = QLabel('Enter width:')
        self.width_label.setFont(font)
        layout.addWidget(self.width_label, 1, 0)
        
        self.width_line = QLineEdit()
        self.width_line.setFont(font)
        layout.addWidget(self.width_line, 1, 1)

        self.height_label = QLabel('Enter height:')
        self.height_label.setFont(font)
        layout.addWidget(self.height_label, 2, 0)
        
        self.height_line = QLineEdit()
        self.height_line.setFont(font)
        layout.addWidget(self.height_line, 2, 1)

        self.solve_area_button = QPushButton('Calculate Surface Area')
        self.solve_area_button.setFont(font)
        self.solve_area_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.solve_area_button.clicked.connect(self.calculate_surface_area)
        layout.addWidget(self.solve_area_button, 3, 0)

        self.solve_volume_button = QPushButton('Calculate Volume')
        self.solve_volume_button.setFont(font)
        self.solve_volume_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.solve_volume_button.clicked.connect(self.calculate_volume)
        layout.addWidget(self.solve_volume_button, 3, 1)

        self.result_label = QLabel('Result:')
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        layout.addWidget(self.result_label, 4, 0)

        self.result_area = QTextEdit()
        self.result_area.setFont(font)
        self.result_area.setReadOnly(True)
        self.result_area.setStyleSheet("background-color: #f0f0f0; border: 1px solid #87CEEB;")
        layout.addWidget(self.result_area, 4, 1, 1, 2)
        
        self.back_home_button = QPushButton('Back to Homepage')
        self.back_home_button.setFont(font)
        self.back_home_button.setToolTip('Exit to the home page')
        self.back_home_button.setShortcut('Escape')
        self.back_home_button.setStyleSheet("background-color: #FF6347; color: white;")
        self.back_home_button.clicked.connect(self.showHomePage)
        layout.addWidget(self.back_home_button, 5, 1)

        self.setLayout(layout)

    def calculate_surface_area(self):
        try:
            length = float(self.length_line.text())
            width = float(self.width_line.text())
            height = float(self.height_line.text())
            surface_area = 2 * (length * width + width * height + height * length)
            self.result_area.setText(f'Surface Area: {surface_area}')
        except Exception as e:
            self.result_area.setText(f'Error: {e}')

    def calculate_volume(self):
        try:
            length = float(self.length_line.text())
            width = float(self.width_line.text())
            height = float(self.height_line.text())
            volume = length * width * height
            self.result_area.setText(f'Volume: {volume}')
        except Exception as e:
            self.result_area.setText(f'Error: {e}')

    def showHomePage(self):
        self.parent().setCurrentWidget(self.parent().parent().home_page)
