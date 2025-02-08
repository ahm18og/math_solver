# home_page.py
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from basic_solver import BasicSolver
from algebraic_solver import AlgebraicSolver
from rectangular_solver import RectangularSolver
from pythagorean_theorem_solver import PythagoreanTheoremSolver
from arc_length_solver import ArcLengthSolver

class MathSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Math Equation Solver Software')
        self.setWindowIcon(QIcon('./res/icon.png'))
        self.setFixedSize(600, 500)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_page = QWidget()
        self.basic_solver_page = BasicSolver()
        self.algebraic_solver_page = AlgebraicSolver()
        self.rectangular_solver_page = RectangularSolver()
        self.pythagorean_solver_page = PythagoreanTheoremSolver()
        self.arc_length_solver_page = ArcLengthSolver()

        self.initHomePageUI()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.basic_solver_page)
        self.stacked_widget.addWidget(self.algebraic_solver_page)
        self.stacked_widget.addWidget(self.rectangular_solver_page)
        self.stacked_widget.addWidget(self.pythagorean_solver_page)
        self.stacked_widget.addWidget(self.arc_length_solver_page)

        self.stacked_widget.setCurrentWidget(self.home_page)

    def initHomePageUI(self):
        layout = QGridLayout()

        font = QFont()
        font.setPointSize(14)

        # Basic Math Button
        self.basic_button = QPushButton('Basic Math')
        self.basic_button.setFont(font)
        self.basic_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.basic_button.clicked.connect(self.showBasicSolver)
        layout.addWidget(self.basic_button, 0, 0)

        # Algebraic Equation Button
        self.algebraic_button = QPushButton('Algebraic Equation')
        self.algebraic_button.setFont(font)
        self.algebraic_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.algebraic_button.clicked.connect(self.showAlgebraicSolver)
        layout.addWidget(self.algebraic_button, 0, 1)

        # Rectangular Area Button
        self.rectangular_button = QPushButton('Rectangular Area')
        self.rectangular_button.setFont(font)
        self.rectangular_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.rectangular_button.clicked.connect(self.showRectangularSolver)
        layout.addWidget(self.rectangular_button, 1, 0)

        # Pythagorean Theorem Button
        self.pythagorean_button = QPushButton('Pythagorean Theorem')
        self.pythagorean_button.setFont(font)
        self.pythagorean_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.pythagorean_button.clicked.connect(self.showPythagoreanTheorem)
        layout.addWidget(self.pythagorean_button, 1, 1)

        # Calculate Arc Length / Area of Sector Button
        self.arc_length_button = QPushButton('Calculate Arc Length / Area of Sector')
        self.arc_length_button.setFont(font)
        self.arc_length_button.setStyleSheet("background-color: #87CEEB; color: white;")
        self.arc_length_button.clicked.connect(self.showArcLengthSolver)
        layout.addWidget(self.arc_length_button, 2, 0)

        # Quit Button
        self.quit_button = QPushButton('Quit')
        self.quit_button.setFont(font)
        self.quit_button.setStyleSheet("background-color: #FF6347; color: white;")
        self.quit_button.clicked.connect(self.exitOut)
        layout.addWidget(self.quit_button, 2, 1)

        self.home_page.setLayout(layout)

    def showBasicSolver(self):
        self.stacked_widget.setCurrentWidget(self.basic_solver_page)

    def showAlgebraicSolver(self):
        self.stacked_widget.setCurrentWidget(self.algebraic_solver_page)

    def showRectangularSolver(self):
        self.stacked_widget.setCurrentWidget(self.rectangular_solver_page)

    def showPythagoreanTheorem(self):
        self.stacked_widget.setCurrentWidget(self.pythagorean_solver_page)

    def showArcLengthSolver(self):
        self.stacked_widget.setCurrentWidget(self.arc_length_solver_page)

    def exitOut(self):
        sys.exit(QApplication(sys.argv))

def main():
    app = QApplication(sys.argv)
    solver = MathSolver()
    solver.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
