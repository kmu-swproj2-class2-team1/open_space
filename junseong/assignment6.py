import pickle
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, \
    QLineEdit


class ScoreDB:
    def __init__(self):
        self.db_path = 'data/assignment6.dat'
        self.scores = []
        self.read()

    def read(self):
        try:
            f = open(self.db_path, 'rb')
            self.scores = pickle.load(f)
            f.close()
        except FileNotFoundError as e:
            print("DB path is wrong")

    # write the data into person db
    def save(self):
        f = open(self.db_path, 'wb')
        pickle.dump(self.scores, f)
        f.close()

    def find(self, name):
        profiles = [profile for profile in self.scores if profile["Name"] == name]
        if len(profiles) == 0:
            raise ProfileNotFound
        return profiles

    def delete(self, name):
        delete_candidate = [index for index, profile in enumerate(self.scores) if profile["Name"] == name]
        if len(delete_candidate) == 0:
            raise ProfileNotFound
        for index in delete_candidate:
            del self.scores[index]

    def add(self, name, age, score):
        profile = {"Name": name, "Age": age, "Score": score}
        self.scores.append(profile)

    def increase(self, name, amount):
        inc_index = [index for index, profile in enumerate(self.scores) if profile["Name"] == name]
        if len(inc_index) == 0:
            raise ProfileNotFound
        for index in inc_index:
            self.scores[index]["Score"] += amount

    def show(self, key):
        return sorted(self.scores, key=lambda profile: profile[key])

    def profile2text(self, profiles=None):
        result = ""
        if profiles is None:
            profiles = self.scores
        for profile in profiles:
            text = "Age=%d\tName=%10s\tScore=%d\n" % (profile["Age"], profile["Name"], profile["Score"])
            result += text
        return result


class InputNoneException(Exception):
    def __init__(self):
        self.msg = "Please Enter Value to Input Field"

    def __str__(self):
        return self.msg


class ProfileNotFound(Exception):
    def __init__(self):
        self.msg = "Profile Not Found"

    def __str__(self):
        return self.msg


class ProfileView(QWidget):
    def __init__(self):
        super().__init__()
        self.db = ScoreDB()
        self.input_ui = {
            "name": {
                "text": "Name :",
            },
            "age": {
                "text": "Age :",
            },
            "score": {
                "text": "Score :",
            },
            "amount": {
                "text": "Amount :",
            }
        }
        self.key_ui = {
            "text": "Key :"
        }
        self.button_ui = {
            "Add": {
                "callback": self.add_clicked
            },
            "Del": {
                "callback": self.del_clicked
            },
            "Find": {
                "callback": self.find_clicked
            },
            "Inc": {
                "callback": self.inc_clicked
            },
            "show": {
                "callback": self.show_clicked
            }
        }
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        # input texts initialize
        input_boxs = QHBoxLayout()
        input_boxs.addStretch(1)
        key_boxs = QHBoxLayout()
        key_boxs.addStretch(1)
        for key, value in self.input_ui.items():
            label = QLabel(value["text"])
            edit = QLineEdit("")
            self.input_ui[key]["edit"] = edit
            if key == "amount":
                key_boxs.addWidget(label)
                key_boxs.addWidget(edit)
            else:
                input_boxs.addWidget(label)
                input_boxs.addWidget(edit)
        vbox.addLayout(input_boxs)

        # Combo box initialize
        key_label = QLabel(self.key_ui["text"], self)
        combo_box = QComboBox(self)
        combo_box.addItems(["Name", "Age", "Score"])
        self.key_ui["combo_box"] = combo_box
        key_boxs.addWidget(key_label)
        key_boxs.addWidget(combo_box)
        vbox.addLayout(key_boxs)

        # buttons initialize
        button_boxs = QHBoxLayout()
        button_boxs.addStretch(1)
        for key, value in self.button_ui.items():
            button = QPushButton(key, self)
            button.clicked.connect(value["callback"])
            button_boxs.addWidget(button)
        vbox.addLayout(button_boxs)

        # result text initialize
        vbox.addWidget(QLabel("Result :"))
        self.result_text = QTextEdit("", self)
        vbox.addWidget(self.result_text)

        # window initialize
        self.setLayout(vbox)
        self.setGeometry(300, 300, 550, 400)
        self.setWindowTitle('Assignment6')
        self.show()
        self.show_result()

    def closeEvent(self, event):
        self.db.save()

    def add_clicked(self):
        try:
            name = self.get_input("name")
            age = int(self.get_input("age"))
            score = int(self.get_input("score"))
            self.db.add(name, int(age), int(score))
            self.show_result()
        except ValueError:
            self.show_error("Please Enter Integer to Age & Score")
        except InputNoneException as e:
            self.show_error(e)

    def del_clicked(self):
        try:
            name = self.get_input("name")
            self.db.delete(name)
            self.show_result()
        except InputNoneException as e:
            self.show_error(e)
        except ProfileNotFound as e:
            self.show_error(e)

    def find_clicked(self):
        try:
            name = self.get_input("name")
            profiles = self.db.find(name)
            self.show_result(profiles=profiles)
        except InputNoneException as e:
            self.show_error(e)
        except ProfileNotFound as e:
            self.show_error(e)

    def inc_clicked(self):
        try:
            name = self.get_input("name")
            amount = int(self.get_input("amount"))
            self.db.increase(name, amount)
            self.show_result()
        except ValueError:
            self.show_error("Please Enter Integer to Amount")
        except InputNoneException as e:
            self.show_error(e)
        except ProfileNotFound as e:
            self.show_error(e)

    def show_clicked(self):
        key = self.key_ui["combo_box"].currentText()
        profiles = self.db.show(key)
        self.show_result(profiles=profiles)

    def show_result(self, profiles=None):
        self.result_text.setText(self.db.profile2text(profiles))

    def show_error(self, error_msg):
        self.result_text.setText("Error: " + str(error_msg))

    def get_input(self, key):
        input_text = self.input_ui[key]["edit"].text()
        if input_text == "":
            raise InputNoneException
        return input_text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProfileView()
    sys.exit(app.exec_())
