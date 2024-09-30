import mysql.connector
from geopy.distance import geodesic
from random import randint
import time
import os

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

# Done by Omar
def player_exists(name):
    sql = "select count(screen_name) from game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result[0] > 0

# Done by Omar
def get_count_of_players():
    sql = "select count(id) from game;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    return result[0]

# Done by Omar
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

# Done by Omar
def get_points(name):
    sql = "select points from game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()

    return result[0]

# Done by Omar
def change_points(name):
    sql = "update game set game.points = (game.points + 1) where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "You have won one point!"

# Done by Omar
def default_settings(name):
    sql = "update game set game.points = 0, game.co2_consumed = 0, game.location = 'EFHK' where screen_name = %s" 
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "Players values set to default"

# Done by Omar
def random_events():
    random_event = randint(1, 3)
    if random_event == 1:
        print("\n⚠️  You’ve encountered a storm mid-flight! Make the right decision to pass safely.")
        print("1. Fly above the storm.")
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
        print("3. Ascend to a higher altitude to avoid the turbulence.")
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
        print("2. Check the instruments to assess the damage.")
        print("3. Call for emergency assistance while flying level.")
        choice = int(input("Choose 1, 2 or 3: "))
        if choice in [1, 3]:
            print("💥 Bad choice! Without understanding the issue, your plane loses control.")
            return 2
        elif choice == 2:
             print("✅ Good choice! You assess the situation and stabilize the flight.")
             return 1

# Done by Omar
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

# Done by Omar    
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

# Done by Omar
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

# Done by Omar
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

# Done by Omar
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

# Done by Omar
def airplane_shape():
    airplane_shape = r"""
       __|__
--o--o--´O`--o--o--
        """
    print (airplane_shape)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[F\033[K', end='')

name = input("Hey there! What's your name? ")
while True:
    add_player(name)
    current_location = get_location(name)
    points = get_points(name)
    fuel = get_fuel(name)
    destination = input(f"You're currently at {current_location[1]} with a fuel budget of {fuel[0]}. Where would you like to fly next? ")
    make_sure = input(f"Fuel usage: {fuel[1]} units. Do you want to keep going? (Y/N): ")
    if make_sure.upper() == "Y":
        airplane_shape()
        events = random_events()
        if events == 1:
            change_points(name)
            change_fuel(name, destination)
            change_location(destination, name)
        else:
            default_settings(name)
            break
    else:
        print("No worries! Until next time!")
        default_settings(name)
        break
    points = get_points(name)
    current_location = get_location(name)
    fuel = get_fuel(name)
    print (f"Welcome! You've just arrived at {current_location[1]}!")
    print (f"Congratulations! You've earned a point. Your total points are now {points}.")
    travle_again = input(f"Your fuel consumption is at {fuel[1]} units. Do you want to embark on another journey? (Y/N): ")
    if travle_again.upper() == "Y":
        print("Awesome! Let's continue the adventure!")
        continue
    else:
        print("No worries! Until next time!")
        default_settings(name)
        break

# print (change_fuel("Heini"))
# print (airport_distance("Helsinki Vantaa Airport"))
# print (get_fuel("Heini"))
# print (get_location("Heini"))
# print (change_location("London Gatwick Airport", "Heini"))