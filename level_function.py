import function
import random
import time
import os



def level_one(name):
    while True:
        current_location = function.get_location(name)
        if current_location is None:
            print("Error: Unable to retrieve current location. Please check your player data.")
            return

        print("Level 1")
        country_code = input(f"You're currently at {current_location[1]}. Which country would you like to explore next? Enter the country code (e.g., US, FI): ")
        airports = function.get_airport_list(country_code)
        for airport in airports:
            print (f"{airport[0]}: {airport[1]}")
        destination = input("Ready for takeoff? Enter the airport ID of your destination: ")
        time.sleep(1)
        function.airplane_shape()
        print("The weather is clear! Take off will be easy.")
        time.sleep(3)
        function.clear_line()
        print("Taking off! Grab your controls and get ready to take off!")
        time.sleep(3)
        if function.press_arrow_keys_fast(3.0) == 1: 
            function.change_point_win(name)
            print("+1 point")
            time.sleep(4)
            function.clear_line()

        events = function.random_events(1)
        if events == 1:
            function.change_point_win(name)
            print("+1 point")
            time.sleep(3)
            function.clear_line()

            print("Get ready to manevuer the plane during the troubles.")
            time.sleep(3)
            if function.press_arrow_keys_fast(3.0) == 1:
                function.change_point_win(name)
                print("+1 point")
                time.sleep(3)
                function.clear_line()
    
            print("Landing time! The weather is sunny. Landing will be easy. Grab your controls and get ready to land the plane!")
            time.sleep(4)
            if function.press_arrow_keys_fast(3.0) == 1: 
                function.change_point_win(name)
                print("+1 point")
                time.sleep(2)
                function.clear_line()
                print("Well done! Moving onto the next level.")
            function.change_location(destination, name)
            time.sleep(3)
            function.clear_line()

            break
        else:
            time.sleep(3)
            function.clear_line()

            print("Level failed. Restarting level!")
            time.sleep(3)
            function.clear_line()

            function.default_settings(name)
            continue


def level_two(name):
    points = function.get_points(name)
    while True:
        current_location = function.get_location(name)
        print(f"Level 2, the game is going to get more difficult!. You have {points} points")
        country_code = input(f"You're currently at {current_location[1]}. Which country would you like to explore next? Enter the country code (e.g., US, FI): ")
        airports = function.get_airport_list(country_code)
        for airport in airports:
            print (f"{airport[0]}: {airport[1]}")
        destination = input("Ready for takeoff? Enter the airport ID of your destination: ")
        time.sleep(1)
        function.airplane_shape()
        print("The weather is cloudy! Take off will be a little more difficult.")
        time.sleep(3)
        function.clear_line()
        print("Taking off! Grab your controls and get ready to take off!")
        time.sleep(3)
        if function.press_arrow_keys_fast(2.5) == 1: 
            function.change_point_win(name)
            print("+1 point")
            time.sleep(4)
            function.clear_line()

        events = function.random_events(2)
        if events == 1:
            function.change_point_win(name)
            print("+1 point")
            time.sleep(3)
            function.clear_line()

            print("Get ready to manevuer the plane during the troubles.")
            time.sleep(3)
            if function.press_arrow_keys_fast(2.5) == 1:
                function.change_point_win(name)
                print("+1 point")
                time.sleep(3)
                function.clear_line()
    
            print("Landing time! The weather is cloudy. Landing will be a little more difficult. Grab your controls and get ready to land the plane!")
            time.sleep(4)
            if function.press_arrow_keys_fast(2.5) == 1: 
                function.change_point_win(name)
                print("+1 point")
                time.sleep(2)
                function.clear_line()
                print("Well done! Moving onto the next level.")
            function.change_location(destination, name)
            time.sleep(3)
            function.clear_line()
            break
        else:
            time.sleep(3)
            function.clear_line()
            print("Level failed. Restarting level!")
            time.sleep(3)
            function.clear_line()
            points
            continue 
