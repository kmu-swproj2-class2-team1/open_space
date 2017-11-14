
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
import math


class Button(QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class NumberButton(Button):
    def __init__(self, number, callback):
        super().__init__(str(number))
        self.number = number
        self.clicked.connect(lambda: callback(self.number))


class ConstantButton(NumberButton):
    def __init__(self, name, number, callback):
        super().__init__(name, callback)
        self.number = number


class OperationButton(Button):
    def __init__(self, op, callback):
        super().__init__(str(op))
        self.op = op
        self.clicked.connect(lambda: callback(self.op))

    def set_priority(self, op):
        if op in ["/", "*"]:
            return 2


class FunctionButton(OperationButton):
    def __init__(self, text, op, callback):
        super().__init__(text, callback)
        self.op = op


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()
        self.number_que = []
        self.number_tmp = []
        self.op_que = []
        self.total_que = []

    def num_btn_callback(self, number):
        self.number_tmp.append(number)
        self.total_que.append(number)
        self.update_view()

    def op_btn_callback(self, op):
        if len(self.total_que) != 0 and type(self.total_que[-1]) == int:
            self.op_que.append(op)
            number = 0
            for i in range(len(self.number_tmp)):
                number += (i + 1) * self.number_tmp[i]
            self.number_que.append(number)
            self.total_que.append(op)
            self.update_view()

    def update_view(self):
        display_text = "".join([str(item) for item in self.total_que])
        self.display.setText(display_text)

    def show_result(self, result):
        self.display.setText(str(result))

    def clear(self, _):
        self.op_que.clear()
        self.total_que.clear()
        self.number_que.clear()
        self.update_view()

    def function_clicked(self, op):
        self.op_btn_callback(op)
        if op == "fact":
            self.factorial()
        elif op == "bin":
            self.binary()
        elif op == "bin2dec":
            self.binary2dec()

    def calculate(self):
        pass

    def factorial(self):
        result = math.factorial(self.number_que[0])
        self.clear(None)
        self.number_que.append(result)
        self.total_que.append(str(result))
        self.update_view()

    def binary(self):
        result = bin(self.number_que[0])
        self.clear(None)
        self.number_que.append(result)
        self.total_que.append(str(result))
        self.update_view()

    def binary2dec(self):
        result = int(self.number_que[0], 2)
        self.clear(None)
        self.number_que.append(result)
        self.total_que.append(str(result))
        self.update_view()

    def init_ui(self):
        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButtons = [NumberButton(x, self.num_btn_callback) for x in range(0, 10)]

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        # numLayout
        numLayout = QGridLayout()
        numLayout.addWidget(self.digitButtons[0], 3, 0)
        numLayout.addWidget(OperationButton('.', self.op_btn_callback), 3, 1)
        numLayout.addWidget(OperationButton('=', self.calculate), 3, 2)
        index = 1
        for i in range(2, -1, -1):
            for j in range(0, 3):
                numLayout.addWidget(self.digitButtons[index], i, j)
                index += 1
        mainLayout.addLayout(numLayout, 1, 0)

        # opLayout
        opLayout = QGridLayout()
        ops = ['*', '/', '+', '-', '(', ')']
        index = 0
        for i in range(0, 3):
            for j in range(2):
                opLayout.addWidget(OperationButton(ops[index], self.op_btn_callback), i, j)
                index += 1
        opLayout.addWidget(OperationButton('C', self.clear), 3, 0)
        mainLayout.addLayout(opLayout, 1, 1)

        extraLayout = QGridLayout()
        constants = [
            ConstantButton("PI", 3.141592, self.num_btn_callback),
            ConstantButton("빛의 이동 속도 (m/s)", 3e+8, self.num_btn_callback),
            ConstantButton("소리의 이동 속도 (m/s)", 340, self.num_btn_callback),
            ConstantButton("태양과의 평균 거리 (km)", 1.5e+8, self.num_btn_callback)
        ]

        functions = [
            FunctionButton("Factorial", "fact", self.function_clicked),
            FunctionButton("-> binary", "bin", self.function_clicked),
            FunctionButton("binary -> dec", "bin2dec", self.function_clicked),
            FunctionButton("-> roman", "rom", self.function_clicked)
        ]

        for i in range(4):
            extraLayout.addWidget(constants[i], i, 0)
            extraLayout.addWidget(functions[i], i, 1)
        mainLayout.addLayout(extraLayout, 2, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
