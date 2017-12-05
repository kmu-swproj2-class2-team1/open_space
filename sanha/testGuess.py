# homework 171204 - using Assert, unittest to test guess(), displayCurrent() and displayGuessed()

import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testGuessCase(self):                       # using Assert to test cases of guess()
        alphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        default_alphabet_List = ['d','e','f','a','u','l','t']
        not_default_alphabet_List = alphabetList - default_alphabet_List

        self.assertTrue(self.g1.guess(x for x in default_alphabet_List))

        self.assertFalse(Self.g1.guess(x for x in not_default_alphabet_List))

        self.assertEqual(self.g1.currentStatus, self.g1.secretWord)

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')          # test init status
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

if __name__ == '__main__':
    unittest.main()
