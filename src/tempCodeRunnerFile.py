# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtGui import QFont
from basic_solver import BasicSolver
from algebraic_solver import AlgebraicSolver
from rectangular_solver import RectangularSolver

class MathSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Math Equation Solver Software')
        self.setFixedSize(600, 500)
        self.setGeometry(200, 200, 600, 500)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_page = QWidget()
        self.basic_solver_page = BasicSolver()
        self.algebraic_solver_page = AlgebraicSolver()
        self.rectangular_solver_page = RectangularSolver()

        self.initHomePageUI()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.basic_solver_page)
        self.stacked_widget.addWidget(self.algebraic_solver_page)
        self.stacked_widget.addWidget(self.rectangular_solver_page)

        self.stacked_widget.setCurrentWidget(self.home_page)

    def initHomePageUI(self):
        layout = QVBoxLayout()

        font = QFont()
        font.setPointSize(14)

        self.basic_button = QPushButton('Basic Math')
        self.basic_button.setFont(font)
        self.basic_button.clicked.connect(self.showBasicSolver)
        layout.addWidget(self.basic_button)

        self.algebraic_button = QPushButton('Algebraic Equation')
        self.algebraic_button.setFont(font)
        self.algebraic_button.clicked.connect(self.showAlgebraicSolver)
        layout.addWidget(self.algebraic_button)

        self.rectangular_button = QPushButton('Calculate Rectangular Area')
        self.rectangular_button.setFont(font)
        self.rectangular_button.clicked.connect(self.showRectangularSolver)
        layout.addWidget(self.rectangular_button)

        self.home_page.setLayout(layout)

    def showBasicSolver(self):
        self.stacked_widget.setCurrentWidget(self.basic_solver_page)

    def showAlgebraicSolver(self):
        self.stacked_widget.setCurrentWidget(self.algebraic_solver_page)

    def showRectangularSolver(self):
        self.stacked_widget.setCurrentWidget(self.rectangular_solver_page) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    solver = MathSolver()
    solver.show()
    sys.exit(app.exec_())
