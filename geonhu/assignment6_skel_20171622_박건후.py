import pickle
import sys
import traceback

from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import *


class UserNotFound(Exception):
    def __init__(self):
        super()



class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.scdb=self.readScoreDB()
        print(self.scdb)
        self.initUI()
        self.showScoreDB('Name')

    def initUI(self):

        ##name, age, score
        name = QLabel('Name : ')
        age = QLabel('Age : ')
        score = QLabel('Score : ')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        line1Layout=QHBoxLayout()
        line1Layout.addWidget(name)
        line1Layout.addWidget(self.nameEdit)
        line1Layout.addWidget(age)
        line1Layout.addWidget(self.ageEdit)
        line1Layout.addWidget(score)
        line1Layout.addWidget(self.scoreEdit)

        ##amount
        amount = QLabel('Amount : ')
        self.amountEdit = QLineEdit()

        key = QLabel('Key : ')
        self.combo = QComboBox()
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")

        line2Layout=QHBoxLayout()
        line2Layout.addStretch(1)
        line2Layout.addWidget(amount)
        line2Layout.addWidget(self.amountEdit)
        line2Layout.addWidget(key)
        line2Layout.addWidget(self.combo)



        ##button
        addButton=QPushButton("Add")
        delButton=QPushButton("Del")
        findButton=QPushButton("Find")
        incButton=QPushButton("Inc")
        showButton=QPushButton("Show")

        addButton.clicked.connect(self.addButtonClicked)
        delButton.clicked.connect(self.delButtonClicked)
        findButton.clicked.connect(self.findButtonClicked)
        incButton.clicked.connect(self.incButtonClicked)
        showButton.clicked.connect(self.showButtonClicked)

        line3Layout=QHBoxLayout()
        line3Layout.addWidget(addButton)
        line3Layout.addWidget(delButton)
        line3Layout.addWidget(findButton)
        line3Layout.addWidget(incButton)
        line3Layout.addWidget(showButton)
        line3Layout.addStretch(0.5)

        ##result

        result=QLabel('Result : ')
        self.showText=QTextEdit()

        line4Layout=QHBoxLayout()
        line4Layout.addWidget(result)

        line5Layout=QHBoxLayout()
        line5Layout.addWidget(self.showText)

        vbox=QVBoxLayout()
        vbox.addLayout(line1Layout)
        vbox.addLayout(line2Layout)
        vbox.addLayout(line3Layout)

        vbox.addLayout(line4Layout)
        vbox.addLayout(line5Layout)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.setLayout(vbox)
        self.show()


    def addButtonClicked(self):
        try:
            record = {'Name': str(self.nameEdit.text()),'Age': int(self.ageEdit.text()),'Score': int(self.scoreEdit.text())}
            self.scdb.append(record)

        except:
            print("Unknown exception occured")

    def delButtonClicked(self):
        try:
            name = self.nameEdit.text()
            userCount=0
            for row in self.scdb:
                if row["Name"] == name:
                    userCount+=1
                    self.scdb.remove(row)

            if userCount==0:
                raise UserNotFound

        except UserNotFound:
            print("No such user, check the user name")

        except IndexError:
            # if user didn't gave the name info
            print("please enter the name with del command")
            print("ex : del Junseong")

        else:
            print("Unknown exception occured")

    def findButtonClicked(self):
        temp = ""
        try:
            name = self.nameEdit.text()
            for row in self.scdb:
                if row['Name']==name:
                    temp+="Age : "+str(row['Age'])+"     Name : "+str(row['Name'])+"      Score : "+str(row['Score'])+'\n'

            self.showText.setPlainText(temp)
        except UserNotFound:
            print("No such user, check the user name")

        except IndexError:
            # if user didn't gave the name info
            print("please enter the name with find command")
            print("ex : find Junseong")

        else:
            print("Unknown exception occured")

    def incButtonClicked(self):
        try:
            name = self.nameEdit.text()

            for row in self.scdb:
                if row['Name'] == name:
                    row['Score'] = row['Score'] + int(self.amountEdit.text())

        except UserNotFound:
            print("No such user, check the user name")


    def showButtonClicked(self):
        try:
            print(self.combo.currentText(),type(self.combo.currentText()) )
            self.showScoreDB(str(self.combo.currentText()))

        except :
            print(sys.exc_info()[0])



    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            scoredb = []
            return
        scoredb= []
        try:
            scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

        # for row in scoredb:
        #     row['Score'] = int(row['Score'])
        #     row['Age'] = int(row['Age'])
        #     print(row['Name'],row['Score'],row['Age'])

        return scoredb

    # write the data into person db
    def writeScoreDB(self):
        print(self.scdb)
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def showScoreDB(self,keyname):
        temp=""
        for p in sorted(self.scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                temp+=attr + "=" + str(p[attr])+"       "
            temp+="\n"
        self.showText.setPlainText(temp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





