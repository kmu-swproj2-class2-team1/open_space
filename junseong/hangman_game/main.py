from game import HangmanGame

game = HangmanGame()
game.new_game()
game.show_state()
while True:
    c = input("Enter Character :")
    result = game.query(c)

    game.show_state()
    if result is True:
        print("Win!")
        break
    elif result is False:
        print("Lose!")
        print("Answer was %s" % "".join(game.answer))
        break

