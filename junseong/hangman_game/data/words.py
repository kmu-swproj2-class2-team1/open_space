from random import choice


class HangmanWords:
    def __init__(self):
        self.words = [word[:-2] for word in open("data/words.txt", "r", encoding="utf-8").readlines()]

    def new_word(self):
        return choice(self.words)
