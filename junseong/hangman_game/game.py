from view import HangmanView
from data.words import HangmanWords


class HangmanGame:
    def __init__(self):
        self.view = HangmanView()
        self.words = HangmanWords()
        self.tries = 0
        self.answer = []
        self.query_str = []
        self.selected_character = []

    def new_game(self):
        self.clear()
        new_word = self.words.new_word()
        self.answer = list(new_word)
        self.query_str = ["_" for _ in range(len(new_word))]
        self.view.update(self.get_state())

    def query(self, c):
        try:
            # 이미 선택되었는가?
            if self.is_selected(c):
                raise AlreadySelected

            else:
                self.selected_character.append(c)

            # c가 정답에 속하는가?
            if c in self.answer:
                self.update_query(c)
                self.view.update(self.get_state())
                if self.is_finished():
                    return True

            else:
                raise WrongAnswer

        except AlreadySelected as e:
            self.view.update(self.get_state(), e)

        except WrongAnswer as e:
            self.tries += 1
            self.view.update(self.get_state(), e)

            if self.is_dead():
                print("\n---------------------------")
                print("Answer was [ %s ]" % "".join(self.answer))
                return False

    def update_query(self, c):
        for i, query_character in enumerate(self.answer):
            if query_character == c:
                self.query_str[i] = c

    def is_selected(self, c):
        return c in self.selected_character

    def is_dead(self):
        return self.tries > 5

    def is_finished(self):
        return "_" not in self.query_str

    def get_state(self):
        return {"tries": self.tries, "query": "".join(self.query_str)}

    def clear(self):
        self.tries = 0
        self.answer.clear()
        self.query_str.clear()
        self.selected_character.clear()


class AlreadySelected(Exception):
    def __init__(self):
        self.message = "Character Already Selected"
        super().__init__(self.message)


class WrongAnswer(Exception):
    def __init__(self):
        self.message = "Wrong Answer"
        super().__init__(self.message)
