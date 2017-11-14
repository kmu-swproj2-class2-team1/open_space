from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
import calcFunctions

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
                if result > 15:
                    self.display.setMaxLength(len(result))
            except:
                result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()
        elif key == constantList[0]:
            self.display.setText(self.display.text() + '3.141592')
        elif key == constantList[1]:
            self.display.setText(self.display.text() + '3E+8')
        elif key == constantList[2]:
            self.display.setText(self.display.text() + '340')
        elif key == constantList[3]:
            self.display.setText(self.display.text() + '1.5E+8')
        elif key == functionList[0]:
            n = self.display.text()
            value = calcFunctions.factorial(n)
            self.display.setText(str(value))
        elif key == functionList[1]:
            n = self.display.text()
            value = calcFunctions.decToBin(n)
            self.display.setText(str(value))
        elif key == functionList[2]:
            n = self.display.text()
            value = calcFunctions.binToDec(n)
            self.display.setText(str(value))
        elif key == functionList[3]:
            n = self.display.text()
            value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
