import level_function
import function
import time

name = input("Enter your name: ")
function.default_settings(name)

while True:

    level_function.level_one(name)
    level_function.level_two(name)
    points = function.get_points(name)
    print(f"You have {points} points")
    print("You win!")
    time.sleep(3)
    break 
