import level_function
import function
import time
import scoreboard

name = input("Enter your name: ")
show_scoreboard = input("Would you like to see the scoreboard? (y/n): ").strip().lower()
if show_scoreboard == 'y':
    scoreboard.display_scoreboard()

function.add_player(name)

while True:

    try:
        level_function.level_one(name)
        level_function.level_two(name)
        points = function.get_points(name)
        print(f"You have {points} points")
        print("You win!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(3)
        break 
