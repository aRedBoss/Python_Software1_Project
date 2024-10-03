import mysql.connector
from geopy.distance import geodesic
from random import randint
import random
import time
import os
import keyboard

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='omar',
    password='Amoury123',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)



def player_exists(name):
    sql = "select count(screen_name) from game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result[0] > 0


def get_count_of_players():
    sql = "select count(id) from game;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    return result[0]


def add_player(name):

    if player_exists(name):
        print("Wellcome back!")
    else:
        count = get_count_of_players()
        player_id = count + 1
        sql = "insert into game (id, co2_consumed, co2_budget, location, screen_name, points) values (%s, %s, %s, %s, %s, %s)"
        values = [player_id, 0, 10000, 'EFHK', name, 0]
        cursor = yhteys.cursor()
        cursor.execute(sql, values)
        yhteys.commit()
        cursor.close()
    return


def get_points(name):
    sql = "select points from game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()

    return result[0]


def change_point_win(name):
    sql = "update game set game.points = (game.points + 1) where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "You have won one point!"


def change_point_lost(name):
    sql = "update game set game.points = (game.points - 1) where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "You have lost one point!"


def default_settings(name):
    sql = "update game set game.points = 0, game.co2_consumed = 0, game.location = 'EFHK' where screen_name = %s" 
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "Players values set to default"

def random_events(level):
    if level == 1:

        while True:  # Loop for level 1
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  You’ve encountered a storm mid-flight! Make the right decision to pass safely.")
                print("1. Fly safely above the storm.")
                print("2. Fly directly through the storm.")
                print("3. Attempt a dangerous emergency landing in the ocean.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Correct! You successfully avoided the storm and continue your journey.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Wrong choice! The plane crashed.")
                    return 2
            elif random_event == 2:
                print("\n🌪️  Alert: You are entering a turbulent zone! Choose your action carefully.")
                print("1. Dive down to a lower altitude to escape the turbulence.")
                print("2. Maintain your current altitude and ride it out.")
                print("3. Ascend to a higher altitude to avoid the turbulence safely.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Wise choice! You ascend and smoothly avoid the turbulence.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! The turbulence worsens, causing damage to the plane.")
                    return 2

            elif random_event == 3:
                print("\n🔧  Alert: You’ve experienced a mechanical failure! Decide how to respond.")
                print("1. Try to land the plane immediately.")
                print("2. Check the instruments to assess the damage and fix it.")
                print("3. Call for emergency assistance while flying level.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 2:
                    print("✅ Good choice! You assess the situation and stabilize the flight.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! Without understanding the issue, your plane loses control.")
                    return 2

    if level == 2:
        while True:  # Loop for level 2
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Warning: A severe thunderstorm is ahead! Choose wisely.")
                print("1. Alter your flight path to navigate around the storm.")
                print("2. Fly into the storm to make up lost time.")
                print("3. Perform an emergency landing on a nearby runway.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Correct! You successfully navigate around the storm.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Wrong choice! The plane is severely damaged in the storm.")
                    return 2
            elif random_event == 2:
                print("\n🌪️  Alert: Unforeseen turbulence is hitting your aircraft! What will you do?")
                print("1. Steer into the turbulence to stabilize the flight.")
                print("2. Pull up sharply to gain altitude quickly.")
                print("3. Release altitude and allow the plane to bounce.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 2:
                    print("✅ Good decision! You gain altitude and smooth out the flight.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Wrong choice! The plane is severely damaged in the storm.")
                    return 2
            elif random_event == 3:
                print("\n🔧  Critical failure alert! A system is malfunctioning! Choose your action.")
                print("1. Ignore it and continue flying.")
                print("2. Check your backup systems.")
                print("3. Initiate emergency protocols immediately.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 2:
                    print("✅ Correct! You check backup systems and regain control.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! The malfunction leads to a crash.")
                    return 2
    if level == 3:
        while True:  # Loop for level 3
            random_event = random.randint(1, 3)
            print("The weather is rainy!")

            if random_event == 1:
                print("\n⚠️  Caution: A volcanic ash cloud is reported in your vicinity! Act fast!")
                print("1. Change course to avoid the ash cloud.")
                print("2. Attempt to fly through the ash to reach clear skies.")
                print("3. Reduce speed to conserve fuel.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Smart move! You steer clear of the ash cloud.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Incorrect choice! The engines are damaged by the ash. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 2:
                print("\n🌪️  Warning: A crosswind is making landing tricky! Decide quickly.")
                print("1. Increase speed to land safely despite the wind.")
                print("2. Attempt a sideways landing.")
                print("3. Circle around and land from the opposite direction.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Wise choice! You successfully land the plane.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! You lose control on landing. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 3:
                print("\n🔧  Alert: A critical gauge has malfunctioned! What will you do?")
                print("1. Fly blindly without checking.")
                print("2. Rely on your instincts to navigate.")
                print("3. Use alternative methods to gauge altitude and speed.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Good call! You use alternative gauges and maintain control.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! You are flying dangerously without information. Restarting level!")
                    continue  # Restart the level if crash happens
    if level == 4:
        while True:  # Loop for level 4
            random_event = random.randint(1, 3)
            print("The weather is windy!")

            if random_event == 1:
                print("\n⚠️  Alert: Severe icing is detected on the wings! Choose carefully.")
                print("1. Climb to a higher altitude to escape the ice.")
                print("2. Use de-icing equipment immediately.")
                print("3. Attempt to glide to a nearby airport.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 2:
                    print("✅ Correct! You successfully de-ice the wings and regain control.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! Climbing worsens the icing condition. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 2:
                print("\n🌪️  Danger: A flock of birds is approaching! What will you do?")
                print("1. Attempt to climb above the birds.")
                print("2. Steer away to avoid collision.")
                print("3. Increase speed to pass through.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 2:
                    print("✅ Wise choice! You avoid a dangerous collision.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! You hit the birds and suffer damage. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 3:
                print("\n🔧  Alert: Fuel reserves are critically low! What will you do?")
                print("1. Search for the nearest airport for an emergency landing.")
                print("2. Try to stretch the fuel by flying lower.")
                print("3. Maintain altitude and conserve fuel.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Good choice! You locate an airport and land safely.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! The plane runs out of fuel. Restarting level!")
                    continue  # Restart the level if crash happens
    if level == 5:
        while True:  # Loop for level 5
            random_event = random.randint(1, 3)
            print("The weather is stormy!")

            if random_event == 1:
                print("\n⚠️  Warning: A ground control communication failure has occurred! Choose wisely.")
                print("1. Attempt to fix the communication systems.")
                print("2. Try to land without guidance.")
                print("3. Use backup systems for navigation.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Smart choice! You regain communication using backups.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! You lose valuable time and crash. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 2:
                print("\n🌪️  Alert: An unexpected wind shear is detected! What will you do?")
                print("1. Pull up immediately to avoid descending.")
                print("2. Maintain current speed and altitude.")
                print("3. Dive down to regain control.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Wise move! You avoid losing altitude.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! You lose control of the aircraft. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 3:
                print("\n🔧  Critical: A cockpit warning light is flashing! Decide your course of action.")
                print("1. Investigate the source of the warning.")
                print("2. Ignore it; it's probably a malfunction.")
                print("3. Call for assistance to analyze the situation.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Good choice! You identify and resolve the issue.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! Ignoring it leads to a crash. Restarting level!")
                    continue  # Restart the level if crash happens
    if level == 6:
        while True:  # Loop for level 6
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Alert: A nearby plane is flying erratically! What will you do?")
                print("1. Maintain your course and speed.")
                print("2. Change altitude to avoid the plane.")
                print("3. Attempt to communicate with the other pilot.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 2:
                    print("✅ Wise choice! You safely avoid a collision.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! Communication failure results in danger. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 2:
                print("\n🌪️  Warning: An unexpected storm cell is forming nearby! Choose your action.")
                print("1. Turn around to avoid the storm entirely.")
                print("2. Use radar to navigate through it.")
                print("3. Dive below to lower altitudes to escape.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Correct! You avoid the storm entirely.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! You end up in the worst part of the storm. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 3:
                print("\n🔧  Alert: A fire is detected in the engine! Decide your action.")
                print("1. Shut down the engine immediately.")
                print("2. Land at the nearest airport.")
                print("3. Use fire suppression systems to contain the fire.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Smart choice! You contain the fire and maintain control.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! The plane loses power. Restarting level!")
                    continue  # Restart the level if crash happens
    if level == 7:
        while True:  # Loop for level 7
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Alert: A critical system failure has occurred mid-flight! Choose wisely.")
                print("1. Attempt a manual override to regain control.")
                print("2. Execute a controlled descent.")
                print("3. Consult with your co-pilot for a strategy.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Good decision! You develop a plan with your co-pilot.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! A controlled descent fails. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 2:
                print("\n🌪️  Caution: An unexpected downdraft is threatening your flight! What will you do?")
                print("1. Pull up sharply to counteract.")
                print("2. Maintain steady speed and altitude.")
                print("3. Lower your flaps for increased lift.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 1:
                    print("✅ Smart choice! You counteract the downdraft effectively.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! Lowering flaps causes instability. Restarting level!")
                    continue  # Restart the level if crash happens
            elif random_event == 3:
                print("\n🔧  Warning: Your navigation system has gone offline! Decide your next step.")
                print("1. Attempt to fix the navigation system.")
                print("2. Rely on visual navigation.")
                print("3. Use emergency radio to contact ground control.")
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == 3:
                    print("✅ Correct! You establish contact and get directions.")
                    return 1
                elif choice > 3:
                    print("Invalid input, try again!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Bad choice! Time wasted leads to a crash. Restarting level!")
                    continue  # Restart the level if crash happens


def get_location(name):
    sql = """  select country.name, airport.name 
                from country 
                inner join airport 
                on country.iso_country = airport.iso_country 
                inner join game 
                on game.location = airport.gps_code 
                where game.screen_name = %s"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result

def get_airport_list(country_code):
    sql ="""select airport.id, airport.name from airport
            inner join country 
            on country.iso_country = airport.iso_country
            where country.iso_country = %s and airport.type = "large_airport";"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()
    cursor.close()

    return result

def check_airport_availability(destination, country_code):
    sql = """select airport.id from airport inner join country on airport.iso_country = country.iso_country where airport.id = %s and country.iso_country = %s;"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (destination, country_code))
    result = cursor.fetchall()
    cursor.close()
    if len(result) == 0:
        return False
    else:
        return True



def change_location(destination, name):
    sql = """  update game 
                join airport on game.location = airport.gps_code 
                join country on country.iso_country = airport.iso_country
                set game.location = (select airport.gps_code from airport where id = %s)
                where game.screen_name = %s;"""
    
    cursor = yhteys.cursor()
    cursor.execute(sql, (destination, name))
    yhteys.commit()
    cursor.close()

    return # (f"Player {name}'s location has been updated to {destination}")


def get_fuel(name):
    sql =   """ select co2_budget, co2_consumed
                from game
                where screen_name = %s;
            """
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result


import random
import time
import os
import keyboard  # Assuming you have keyboard module for key press detection

def press_arrow_keys_fast(num: float):
    arrow_keys = ['up', 'down', 'left', 'right']
    
    # Generate a random sequence of 5 arrow keys, ensuring no consecutive keys are the same
    sequence = []
    while len(sequence) < 5:
        next_key = random.choice(arrow_keys)
        if not sequence or next_key != sequence[-1]:  # Ensure no consecutive keys
            sequence.append(next_key)
    
    # Show the countdown before starting
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    print("Go!\n")
    
    # Start tracking time
    start_time = time.time()

    # Show the sequence to the user one key at a time
    for key in sequence:
        print(f"Press: {key} (You have {num} seconds!)")
        # Wait for the user to press the correct key within the time limit
        key_start_time = time.time()  # Start time for the current key
        while time.time() - key_start_time < num:
            if keyboard.is_pressed(key):
                print("✅ Correct!")
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[F\033[K', end='')
            print("💥 Too slow! No point for you! Moving on.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[F\033[K', end='')
            return 2  # Player failed to press the key in time
    
    # End tracking time
    end_time = time.time()
    
    # Calculate total time taken
    total_time = end_time - start_time

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[F\033[K', end='')
    print(f"✅ Great! You pressed all keys in {total_time:.2f} seconds.")
    
    return 1

def airport_distance(name, destination):
    current_location = get_location(name)
    airport1 = current_location[1]

    airport2 = destination

    cursor = yhteys.cursor()

    sql1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE name = %s"
    cursor.execute(sql1, (airport1,))
    result1 = cursor.fetchone()
    if result1 is None:
        cursor.close()
        return f"Airport {airport1} not found."


    sql2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE id = %s"
    cursor.execute(sql2, (airport2,))
    result2 = cursor.fetchone()
    if result2 is None:
        cursor.close()
        return f"Airport {airport2} not found."

    cursor.close()

    airport1_coords = (result1[0], result1[1])  # (latitude, longitude)
    airport2_coords = (result2[0], result2[1])

    # Calculate the distance using geopy
    distance = geodesic(airport1_coords, airport2_coords).kilometers

    # print(f"Calculated distance from {airport1} to {airport2} is {distance:.2f} km.")

    return distance


def change_fuel(name, destination):
    distance = airport_distance(name, destination)
    fuel_consumed = (distance / 100) * 10
    sql =   """update game
                set co2_consumed = co2_consumed + %s
                where screen_name = %s;
            """
    cursor = yhteys.cursor()
    cursor.execute(sql, (fuel_consumed, name))
    yhteys.commit()
    cursor.close()

    result = f"Player {name} has consumed {int(fuel_consumed)} usnit of fuel"
    # print(result)

    return result

def display_scoreboard():
    sql = "SELECT screen_name, points FROM game ORDER BY points DESC"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()

    print("\nScoreboard:")
    for row in results:
        print(f"Player: {row[0]}, Points: {row[1]}")


def airplane_shape():
    airplane_shape = r"""
       __|__
--o--o--´O`--o--o--
        """
    print (airplane_shape)

def clear_line():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[F\033[K', end='')