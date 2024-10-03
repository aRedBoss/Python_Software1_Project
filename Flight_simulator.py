import level_function
import function
import time

name = input("name ")
function.default_settings(name)

while True:

    level_function.level_one(name)
    level_function.level_two(name)
    level_function.level_three(name)
    level_function.level_four(name)
    level_function.level_five(name)
    points = function.get_points(name)
    print(f"You win with {points} points!")
    time.sleep(3)
    break 