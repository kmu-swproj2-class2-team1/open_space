from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


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


class OperationButton(Button):
    def __init__(self, op, callback):
        super().__init__(str(op))
        self.op = op
        self.clicked.connect(lambda: callback(self.op))

    def set_priority(self, op):
        if op in ["/", "*"]:
            return 2


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
                number+=(i+1)*self.number_tmp[i]
            self.number_que.append(number)
            self.total_que.append(op)
            self.update_view()

    def update_view(self):
        display_text = "".join([str(item) for item in self.total_que])
        self.display.setText(display_text)

    def show_result(self, result):
        self.display.setText(str(result))

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
        numLayout.addWidget(OperationButton('=', self.op_btn_callback), 3, 2)
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
        opLayout.addWidget(OperationButton('C', self.op_btn_callback), 3, 0)
        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My Calculator")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
