# basic_solver.py
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BasicSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        font = QFont()
        font.setPointSize(14)

        # Input label
        self.input_label = QLabel('Enter your math problem:')
        self.input_label.setFont(font)
        layout.addWidget(self.input_label)

        # Input line
        self.input_line = QLineEdit()
        self.input_line.setFont(font)
        self.input_line.setToolTip('You must enter something')
        self.input_line.setPlaceholderText("Enter your basic math problem, i.e. '1 + 1'")
        layout.addWidget(self.input_line)

        # Solve button
        self.solve_button = QPushButton('Solve')
        self.solve_button.setFont(font)
        self.solve_button.setToolTip('Click to solve the problem')
        self.solve_button.setShortcut('Return')
        self.solve_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.solve_button.clicked.connect(self.solve_problem)
        layout.addWidget(self.solve_button)

        # Result label
        self.result_label = QLabel('Result:')
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        layout.addWidget(self.result_label)

        # Result text area
        self.result_area = QTextEdit()
        self.result_area.setFont(font)
        self.result_area.setToolTip('The result will appear here once you press \'Enter\' on your keyboard or click the \'Solve\' button.')
        self.result_area.setPlaceholderText('The result will be written here.')
        self.result_area.setReadOnly(True)
        self.result_area.setStyleSheet("background-color: #f0f0f0; border: 1px solid #87CEEB;")
        layout.addWidget(self.result_area)

        # Back to Homepage button
        self.back_home_button = QPushButton('Back to Homepage')
        self.back_home_button.setFont(font)
        self.back_home_button.setToolTip('Exit to the home page')
        self.back_home_button.setShortcut('Escape')
        self.back_home_button.setStyleSheet("background-color: #FF6347; color: white;")
        self.back_home_button.clicked.connect(self.showHomePage)
        layout.addWidget(self.back_home_button)

        self.setLayout(layout)

    def solve_problem(self):
        problem = self.input_line.text()
        problem = problem.replace('^', '**')
        if not problem.strip():
            self.result_area.setText('Please enter something, and try again!')
        elif problem.strip().isalpha():
            self.result_area.setText('Please enter a number! If you\'re solving for algebra, quit to homepage and use the algebraic equation solver!')
        else:
            try:
                result = eval(problem)
                self.result_area.setText(f'Result: {result}')
            except Exception as e:
                self.result_area.setText(f'Error: {e}')
    
    def showHomePage(self):
        self.parent().setCurrentWidget(self.parent().parent().home_page)
