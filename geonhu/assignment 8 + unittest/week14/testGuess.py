import unittest

# import logging

from week14.guess import Guess



class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testGuess(self):

        # log=logging.getLogger("TestGuess.testGuess")

        # self.g1.guess('')

        self.assertTrue(self.g1.guess('l'))
        self.assertFalse(self.g1.currentStatus is self.g1.secretWord)

        self.assertTrue(self.g1.guess('f'))
        self.assertFalse(self.g1.currentStatus is self.g1.secretWord)

        self.assertTrue(self.g1.guess('a'))
        self.assertFalse(self.g1.currentStatus is self.g1.secretWord)

        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.currentStatus is self.g1.secretWord)

        self.assertTrue(self.g1.guess('u'))
        self.assertFalse(self.g1.currentStatus is self.g1.secretWord)

        self.assertTrue(self.g1.guess('t'))

        #
        # #logging
        # log.debug("sw=%s",self.g1.secretWord)
        # log.debug("cs=%s", self.g1.currentStatus)

        self.assertTrue(self.g1.currentStatus.strip() == self.g1.secretWord.strip(),msg='{0},{1}'.format(self.g1.currentStatus,self.g1.secretWord))


    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u l t ')

        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')

        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')

        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')


if __name__ == '__main__':
    unittest.main()
