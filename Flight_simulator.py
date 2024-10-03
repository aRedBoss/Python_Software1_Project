import level_function
import function
import time

name = input("Hey there, what is your name? ")
function.default_settings(name)

high_score = 1

while True:
    level_function.level_one(name)
    level_function.level_two(name)
    level_function.level_three(name)
    level_function.level_four(name)
    level_function.level_five(name)
    points = function.get_points(name)
    print(f"You finished the game with {points} points!")
    time.sleep(1)
    if points > high_score[0]:
        high_score[0] = points
        print(f"New high score: {high_score} points!")
        time.sleep(2)
    print (f"High score: {high_score} points.")
    time.sleep(1)
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        continue
    elif play_again == "n":
        print("Until next time.")
        time.sleep(1)
        break
    else:
        break
