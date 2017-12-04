import unittest
from game import HangmanGame


class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        self.hangman_game = HangmanGame()

    def testDisplayCurrent(self):
        self.hangman_game.new_game("hello")
        self.assertEqual(self.hangman_game.get_query(), "_____")

        self.hangman_game.query("h")
        self.assertEqual(self.hangman_game.get_query(), "h____")

        self.hangman_game.query("l")
        self.assertEqual(self.hangman_game.get_query(), "h_ll_")

        # 오류 문자 case
        self.hangman_game.query("a")
        self.assertEqual(self.hangman_game.get_query(), "h_ll_")

        # 숫자 문자 case
        self.hangman_game.query("3")
        self.assertEqual(self.hangman_game.get_query(), "h_ll_")

        # 다중 문자 case
        self.hangman_game.query("avdc")
        self.assertEqual(self.hangman_game.get_query(), "h_ll_")

        self.hangman_game.query("o")
        self.assertEqual(self.hangman_game.get_query(), "h_llo")

        self.hangman_game.query("e")
        self.assertEqual(self.hangman_game.get_query(), "hello")

    def testDisplayTries(self):
        self.hangman_game.new_game("hello")
        self.assertEqual(self.hangman_game.get_selected_character(), "")

        self.hangman_game.query("h")
        self.assertEqual(self.hangman_game.get_selected_character(), "h")

        self.hangman_game.query("e")
        self.assertEqual(self.hangman_game.get_selected_character(), "h e")

        self.hangman_game.query("l")
        self.assertEqual(self.hangman_game.get_selected_character(), "h e l")

        # 중복 문자 case
        self.hangman_game.query("l")
        self.assertEqual(self.hangman_game.get_selected_character(), "h e l")

        # 오류 문자 case
        self.hangman_game.query("a")
        self.assertEqual(self.hangman_game.get_selected_character(), "h e l a")

        self.hangman_game.query("o")
        self.assertEqual(self.hangman_game.get_selected_character(), "h e l a o")
