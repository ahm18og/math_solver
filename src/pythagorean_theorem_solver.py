from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

class PythagoreanTheoremSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        font = QFont()
        font.setPointSize(14)

        self.label_a = QLabel('Enter a value:')
        self.label_a.setFont(font)
        layout.addWidget(self.label_a, 0, 0)
        
        self.input_a = QLineEdit()
        self.input_a.setFont(font)
        self.input_a.setPlaceholderText("Enter the a value, e.g. '3'")
        layout.addWidget(self.input_a, 0, 1)

        self.label_b = QLabel('Enter b value:')
        self.label_b.setFont(font)
        layout.addWidget(self.label_b, 1, 0)
        
        self.input_b = QLineEdit()
        self.input_b.setFont(font)
        self.input_b.setPlaceholderText("Enter the b value, e.g. '4'")
        layout.addWidget(self.input_b, 1, 1)

        self.label_c = QLabel('Enter c value:')
        self.label_c.setFont(font)
        layout.addWidget(self.label_c, 2, 0)
        
        self.input_c = QLineEdit()
        self.input_c.setFont(font)
        self.input_c.setPlaceholderText("Enter the c value, e.g. '5'")
        layout.addWidget(self.input_c, 2, 1)

        self.result_label = QLabel('Result:')
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        layout.addWidget(self.result_label, 3, 0)
        
        self.result_display = QLineEdit()
        self.result_display.setFont(font)
        self.result_display.setPlaceholderText('Your answer will show up here.')
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("background-color: #f0f0f0; border: 1px solid #87CEEB;")
        layout.addWidget(self.result_display, 3, 1)

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.setFont(font)
        self.calculate_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button, 4, 1)

        self.back_home_button = QPushButton('Back to Homepage')
        self.back_home_button.setFont(font)
        self.back_home_button.setToolTip('Exit to the home page')
        self.back_home_button.setShortcut('Escape')
        self.back_home_button.setStyleSheet("background-color: #FF6347; color: white;")
        self.back_home_button.clicked.connect(self.showHomePage)
        layout.addWidget(self.back_home_button, 4, 0)

        self.setLayout(layout)

    def calculate(self):
        a = self.input_a.text()
        b = self.input_b.text()
        c = self.input_c.text()

        result = ''
        if a and b and not c:
            a = float(a)
            b = float(b)
            c = math.sqrt(a ** 2 + b ** 2)
            result = f'a = {a}, b = {b} -> c = {c}'
        elif a and c and not b:
            a = float(a)
            c = float(c)
            if c > a:
                b = math.sqrt(c ** 2 - a ** 2)
                result = f'a = {a}, c = {c} -> b = {b}'
            else:
                result = 'Error: c must be greater than a'
        elif b and c and not a:
            b = float(b)
            c = float(c)
            if c > b:
                a = math.sqrt(c ** 2 - b ** 2)
                result = f'b = {b}, c = {c} -> a = {a}'
            else:
                result = 'Error: c must be greater than b'
        else:
            result = 'Please enter only two values.'

        self.result_display.setText(result)

    def showHomePage(self):
        self.parent().setCurrentWidget(self.parent().parent().home_page)
