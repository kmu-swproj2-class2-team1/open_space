from game import HangmanGame

game = HangmanGame()
game.new_game()
while True:
    c = input("Enter Character :")
    result = game.query(c)
    if result is True:
        print("Win!")
        break
    elif result is False:
        print("Lose!")
        break
