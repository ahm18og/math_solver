from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sympy import symbols, Eq, solve

class AlgebraicSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        font = QFont()
        font.setPointSize(14)

        # Styling for input labels and lines
        self.algebraic_input_label = QLabel('Enter your algebraic equation:')
        self.algebraic_input_label.setFont(font)
        layout.addWidget(self.algebraic_input_label)

        self.algebraic_input_line = QLineEdit()
        self.algebraic_input_line.setFont(font)
        self.algebraic_input_line.setPlaceholderText("Enter the algebraic equation to solve, e.g., '2*x + 3*y - 4 = 0'")
        layout.addWidget(self.algebraic_input_line)

        self.variables_label = QLabel('Enter variables (comma separated):')
        self.variables_label.setFont(font)
        layout.addWidget(self.variables_label)

        self.variables_line = QLineEdit()
        self.variables_line.setFont(font)
        self.variables_line.setPlaceholderText("Enter the variables in the equation, e.g., 'x, y'")
        layout.addWidget(self.variables_line)

        # Solve Algebraic Equation Button
        self.solve_algebraic_button = QPushButton('Solve Algebraic Equation')
        self.solve_algebraic_button.setFont(font)
        self.solve_algebraic_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.solve_algebraic_button.clicked.connect(self.solve_algebraic_problem)
        layout.addWidget(self.solve_algebraic_button)

        # Result label
        self.algebraic_result_label = QLabel('Result:')
        self.algebraic_result_label.setFont(font)
        self.algebraic_result_label.setAlignment(Qt.AlignCenter)
        self.algebraic_result_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
        layout.addWidget(self.algebraic_result_label)

        # Result text area
        self.algebraic_result_area = QTextEdit()
        self.algebraic_result_area.setFont(font)
        self.algebraic_result_area.setPlaceholderText('Answer will appear here.')
        self.algebraic_result_area.setReadOnly(True)
        self.algebraic_result_area.setStyleSheet("background-color: #f0f0f0; border: 1px solid #87CEEB;")
        layout.addWidget(self.algebraic_result_area)

        # Back to Homepage Button
        self.back_home_button = QPushButton('Back to Homepage')
        self.back_home_button.setFont(font)
        self.back_home_button.setToolTip('Exit to the home page')
        self.back_home_button.setShortcut('Escape')
        self.back_home_button.setStyleSheet("background-color: #FF6347; color: white;")
        self.back_home_button.clicked.connect(self.showHomePage)
        layout.addWidget(self.back_home_button)

        self.setLayout(layout)

    def solve_algebraic_problem(self):
        eq = self.algebraic_input_line.text()
        var = self.variables_line.text()
        variables = var.replace(' ', '').split(',')
        symbols_list = symbols(variables)
        try:
            equation = eq.replace('=', '-(') + ')'
            eq = eval(equation, {str(sym): sym for sym in symbols_list})
            solutions = solve(eq, symbols_list)
            self.algebraic_result_area.setText(f'Result: {solutions}')
        except Exception as e:
            self.algebraic_result_area.setText(f'Error: {e}')

    def showHomePage(self):
        self.parent().setCurrentWidget(self.parent().parent().home_page)
