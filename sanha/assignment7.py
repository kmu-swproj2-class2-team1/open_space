from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

# 사용자 클래스 (Button) 생성 - 공통된 부분을 클래스에 넣어서 관리

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)        # 사이즈 조정
        self.setText(text)
        self.clicked.connect(callback)             # 버튼이 눌릴 때의 기능 구현

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)             # 사이즈 늘리기
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget) :
    
    def __init__(self, parent = None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()         # Python에서 0으로 시작하는 수는 8진수로 인식하므로 0이 안붙도록 수정
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]               # 버튼 클래스 생성

        for i in range(10) :
            self.digitButton[i] = Button(str([i]), self.buttonClicked)

        # . and = Buttons    
        self.decButton = Button('.', self.buttonClicked)             # callback을 넘겨줘야함
        self.eqButton = Button('=', self.buttonClicked)              ## self.~~~ = Button('~', self.buttonClicked)로

        # Operator Buttons
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)      # 맨 윗줄의 layout이 가로1칸 세로2칸을 차지하겠다는 뜻 (1,2)
        numLayout = QGridLayout()

        # 버튼 생성 부분 (기능을 구현하기 전에 버튼을 추가)

        for i in range(0, 3) :
            for j in range(0, 3):
                numLayout.addWidget(self.digitButton[7+j-3*i], i ,j)

        numLayout.addWidget(self.digitButton[0], 3, 0)
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)


        mainLayout.addLayout(numLayout, 1, 0)
        opLayout = QGridLayout()
        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)
        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)
        opLayout.addWidget(self.clearButton, 3, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")
        
    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


# Main
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
