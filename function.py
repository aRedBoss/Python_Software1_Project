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
        values = [player_id, 0, 10000, 'EFHK', name, 500]
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
        random_event = randint(1, 3)
        if random_event == 1:
            print("\n⚠️  You’ve encountered a storm mid-flight! Make the right decision to pass safely.")
            print("1. Fly safly above the storm.")
            print("2. Fly directly through the storm.")
            print("3. Attempt a dangerous emergency landing in the ocean.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 1:
                print("✅ Correct! You successfully avoided the storm and continue your journey.")
                return 1
            elif choice in [2, 3]:
                print("💥 Wrong choice! The plane crashed.")
                return 2

        elif random_event == 2:
            print("\n🌪️  Alert: You are entering a turbulent zone! Choose your action carefully.")
            print("1. Dive down to a lower altitude to escape the turbulence.")
            print("2. Maintain your current altitude and ride it out.")
            print("3. Ascend to a higher altitude to avoid the turbulence safly.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 3:
                print("✅ Wise choice! You ascend and smoothly avoid the turbulence.")
                return 1
            elif choice in [1, 2]:
                print("💥 Bad choice! The turbulence worsens, causing damage to the plane.")
                return 2
        else:
            print("\n🔧  Alert: You’ve experienced a mechanical failure! Decide how to respond.")
            print("1. Try to land the plane immediately")
            print("2. Check the instruments to assess the damage and fix it.")
            print("3. Call for emergency assistance while flying level.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice in [1, 3]:
                print("💥 Bad choice! Without understanding the issue, your plane loses control.")
                return 2
            elif choice == 2:
                print("✅ Good choice! You assess the situation and stabilize the flight.")
                return 1
    elif level == 2:
        random_event_level2 = random.randint(1, 3)

        if random_event_level2 == 1:
            print("\n🔥 Emergency: One of the engines has caught fire!")
            print("1. Shut down the burning engine and divert to the nearest airport.")
            print("2. Try to extinguish the fire mid-flight.")
            print("3. Increase speed to blow out the fire.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 1:
                print("✅ Smart move! You shut down the engine and land safely.")
                return 1
            elif choice in [2, 3]:
                print("💥 Bad decision! The fire spreads, and the plane crashes.")
                return 2

        elif random_event_level2 == 2:
            print("\n🛩️  You’re running low on fuel in the middle of nowhere!")
            print("1. Look for the nearest airport and attempt an emergency landing.")
            print("2. Try to conserve fuel by reducing speed and altitude.")
            print("3. Call air traffic control and request a fuel dump.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 2:
                print("✅ Good call! You conserve fuel and make it to the nearest airport.")
                return 1
            elif choice in [1, 3]:
                print("💥 Poor decision! You either run out of fuel or lose precious time.")
                return 2

        elif random_event_level2 == 3:
            print("\n❄️  The plane’s wings are icing over, reducing control!")
            print("1. Descend to a warmer altitude to melt the ice.")
            print("2. Engage anti-ice systems and continue as planned.")
            print("3. Perform aggressive maneuvers to shake off the ice.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 2:
                print("✅ Right choice! The anti-ice system works, and you regain control.")
                return 1
            elif choice in [1, 3]:
                print("💥 Wrong choice! The ice buildup worsens, and you lose control of the plane.")
                return 2
    else:
        random_event_level3 = random.randint(1, 3)

        if random_event_level3 == 1:
            print("\n🛰️  Emergency: A satellite debris field is heading your way!")
            print("1. Perform a steep dive to avoid the debris.")
            print("2. Change your flight path slightly and fly through.")
            print("3. Speed up to fly past the debris field before it reaches you.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 3:
                print("✅ Good decision! You speed up and narrowly escape the debris.")
                return 1
            elif choice in [1, 2]:
                print("💥 Bad move! The debris strikes the plane, causing a crash.")
                return 2

        elif random_event_level3 == 2:
            print("\n⚡️ Critical: You are caught in a dangerous electrical storm!")
            print("1. Descend immediately to avoid lightning.")
            print("2. Fly straight through at full speed.")
            print("3. Fly at a steady pace, hoping to ride it out.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 1:
                print("✅ Smart move! Descending keeps you below the worst of the storm, and you avoid disaster.")
                return 1
            elif choice in [2, 3]:
                print("💥 Bad decision! Lightning strikes the plane, causing severe damage.")
                return 2

        elif random_event_level3 == 3:
            print("\n🛑  Alert: A fuel leak has been detected!")
            print("1. Reduce speed immediately to conserve fuel.")
            print("2. Perform a risky emergency landing.")
            print("3. Jettison excess weight to lighten the plane and conserve fuel.")
            choice = int(input("Choose 1, 2 or 3: "))
            if choice == 3:
                print("✅ Excellent choice! You reduce the weight and successfully conserve fuel.")
                return 1
            elif choice in [1, 2]:
                print("💥 Wrong decision! The plane runs out of fuel before you reach safety.")
                return 2


def get_location(name):
    sql = f"""  select country.name, airport.name 
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

  
def change_location(destination, name):
    sql = f"""  update game 
                join airport on game.location = airport.gps_code 
                join country on country.iso_country = airport.iso_country
                set game.location = (select airport.gps_code from airport where name = %s)
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


# Function to randomly ask the user to press arrow keys in a fast sequence
def press_arrow_keys_fast(num):
    arrow_keys = ['up', 'down', 'left', 'right']
    
    # Generate a random sequence of 5 arrow keys
    sequence = random.choices(arrow_keys, k=5)
    
    # Show the countdown before starting
    print("Prepare for the emergency maneuver! You have 3 seconds to brace yourself...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    print("Go!\n")
    
    # Show the sequence to the user one key at a time
    print("Alert! The plane is losing altitude. Quickly press the following arrow keys in order to steer the plane to safety:")
    
    start_time = time.time()  # Start tracking time

    for key in sequence:
        print(f"Press: {key} (You have {num} seconds!)")
        # Wait for the user to press the correct key within 2 seconds
        key_start_time = time.time()  # Start time for the current key
        while time.time() - key_start_time < num:
            if keyboard.is_pressed(key):
                print("✅ Correct!")
                break
        else:
            print("💥 Too slow! Moving to the next key.")
            print(f"The correct key was: {key}")
            return 2  # Player failed to press the key in time
    
    # End tracking time
    end_time = time.time()
    
    # Calculate total time taken
    total_time = end_time - start_time
    
    print(f"Great! You pressed all keys in {total_time:.2f} seconds.")
    return 1  # Player successfully pressed all keys


def airport_distance(name, destination):
    current_location = get_location(name)
    airport1 = current_location[1]

    airport2 = destination

    cursor = yhteys.cursor()

    sql1 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = %s"
    cursor.execute(sql1, (airport1,))
    result1 = cursor.fetchone()
    if result1 is None:
        cursor.close()
        return f"Airport {airport1} not found."


    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = %s"
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
    sql =   f"""update game
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


def airplane_shape():
    airplane_shape = r"""
       __|__
--o--o--´O`--o--o--
        """
    print (airplane_shape)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[F\033[K', end='')