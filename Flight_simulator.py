import function


name = input("Hey there! What's your name? ")
while True:
    function.add_player(name)
    current_location = function.get_location(name)
    points = function.get_points(name)
    fuel = function.get_fuel(name)
    print("Level 1")
    destination = input(f"You're currently at {current_location[1]}. Where would you like to fly next? ")
    function.airplane_shape()
    events = function.random_events(1)
    if events == 1:
        function.change_point_win(name)
        function.change_fuel(name, destination)
        function.change_location(destination, name)
    else:
        function.press_arrow_keys_fast(3)
        if function.press_arrow_keys_fast(3) == 1:
            function.change_point_win(name)
            function.change_fuel(name, destination)
            function.change_location(destination, name)
        else:
            print("You have lost!")
            break
    print("You have passed level 1!")
    fuel = function.get_fuel(name)
    points = function.get_points(name)
    current_location = function.get_location(name)
    print("Level 2")
    destination = input(f"You're currently at {current_location[1]}. Where would you like to fly next? ")
    function.airplane_shape()
    events = function.random_events(2)
    if events == 1:
        function.change_point_win(name)
        function.change_fuel(name, destination)
        function.change_location(destination, name)
    else:
        function.press_arrow_keys_fast(2)
        if function.press_arrow_keys_fast(2) == 1:
            function.change_point_win(name)
            function.change_fuel(name, destination)
            function.change_location(destination, name)
        else:
            print("You have lost!")
            break
    fuel = function.get_fuel(name)
    points = function.get_points(name)
    current_location = function.get_location(name)
    print("You have passed level 2!")
    destination = input(f"You're currently at {current_location[1]}. Where would you like to fly next? ")
    function.airplane_shape()
    events = function.random_events(3)
    if events == 1:
        function.change_point_win(name)
        function.change_fuel(name, destination)
        function.change_location(destination, name)
    else:
        function.press_arrow_keys_fast(1)
        if function.press_arrow_keys_fast(1) == 1:
            function.change_point_win(name)
            function.change_fuel(name, destination)
            function.change_location(destination, name)
        else:
            print("You have lost!")
            break
    print("Congratulations you won the game!")
    break

# print (change_fuel("Heini"))
# print (airport_distance("Helsinki Vantaa Airport"))
# print (get_fuel("Heini"))
# print (get_location("Heini"))
# print (change_location("London Gatwick Airport", "Heini"))