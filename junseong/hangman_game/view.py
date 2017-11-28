from data.character_ui import hangman_ui


class HangmanView:
    def __init__(self):
        self.hangman_ui = hangman_ui

    def update(self, state, error=None):
        self.update_status(state)
        self.update_character(state)
        if error is not None:
            print(error.message)

    def update_status(self, state):
        print("Current: %s" % state["query"])
        print("Tries: %d" % state["tries"])

    def update_character(self, state):
        print(self.hangman_ui[state["tries"]])
