from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
import sys

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)  # 사이즈 늘리기
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        #lineEdit Setting
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(25)


        #계산기 기호 버튼
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton  = Button('=', self.buttonClicked)
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)
        self.leftBracketButton = Button('(', self.buttonClicked)
        self.rightBracketButton = Button(')', self.buttonClicked)
        self.clearButton = Button('C', self.buttonClicked)
        opLayout = QGridLayout()
        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)
        opLayout.addWidget(self.leftBracketButton, 2, 0)
        opLayout.addWidget(self.rightBracketButton, 2, 1)
        opLayout.addWidget(self.clearButton, 3, 0)


        #계산기 숫자 버튼
        self.digitButton = [x for x in range(0, 10)]
        for i in range(10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        numLayout = QGridLayout()
        numLayout.addWidget(self.digitButton[0], 3, 0)
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        for i in range(0, 3):
            for j in range(0, 3):
                numLayout.addWidget(self.digitButton[7 + j - 3 * i], i, j)


        #메인레이아웃 시작
        self.mainLayout = QGridLayout()
        self.mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.mainLayout.addWidget(self.display, 0, 0, 1, 2)
        self.mainLayout.addLayout(numLayout, 1, 0)
        self.mainLayout.addLayout(opLayout, 1, 1)

        #레이아웃 세팅
        self.setLayout(self.mainLayout)
        self.setWindowTitle("20171622_박건후")

    #ButtonClicked 메소드
    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            ##eval SyntaxError 처리
            try:
                result = str(eval(self.display.text()))
            except SyntaxError:
                result="SyntaxError! Press C"
            finally:
                self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())