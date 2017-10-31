import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication, QLabel,
QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = self.readScorDB()
        self.readScoreDB()
        self.showScoreDB('Name')

    def initUI(self):
# Name, Age, Score

        name = QLabel('Name = ')
        age = QLabel('age = ')
        score = QLabel('Score = ')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

# button, box, layout

#button
        app = QApplication(sys.argv)
        print(sys.argv)

        add_Button = QPushButton('Add')
        del_Button = QPushButton('Del')
        find_Button = QPushButton('Find')
        inc_Button = QPushButton('Inc')
        show_Button = QPushButton('Show')



    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')

        except FileNotFoundError as e:
            self.scoredb = []

            return

        self.scoredb = []

        try:
            self.scoredb = pickle.load(fH)

        except:
            pass

        else:
            pass

        fH.close()

        return self.scoredb

# write the data into person db
def writeScoreDB(self):
    fH = open(self.dbfilename, 'wb')
    pickle.dump(self.scoredb, fH)
    fH.close()

def showScoreDB(self):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())