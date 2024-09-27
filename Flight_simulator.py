import mysql.connector
from geopy.distance import geodesic
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

    return (f"Player {name}'s location has been updated to {destination}")

def get_fuel(name):
    sql =   """ select co2_budget, co2_consumed
                from game
                where screen_name = %s;
            """
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()

    return result

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

    print(f"Calculated distance from {airport1} to {airport2} is {distance:.2f} km.")

    return distance

def change_fuel(name, destination):
    distance = airport_distance(name, destination)
    print(destination)
    fuel_consumed = (distance / 100) * 10
    sql =   f"""update game
                set co2_consumed = co2_consumed + %s
                where screen_name = %s;
            """
    cursor = yhteys.cursor()
    cursor.execute(sql, (fuel_consumed, name))
    yhteys.commit()

    result = f"Player {name} has consumed {int(fuel_consumed)} usnit of fuel"
    print(result)

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

while True:
    name = input("What is your name? ")
    current_location = get_location(name)
    fuel = get_fuel(name)
    destination = input(f"You are at {current_location[1]} airport. Your fuel budget is {fuel[0]}. Where would you like to travel? ")
    make_sure = input(f"Your consumed fuel is {fuel[1]}. Would you like to proceed? [y or n] ")
    if make_sure == "y":
        airplane_shape()
        change_fuel(name, destination)
        change_location(destination, name)
    else:
        print("That's unfortunate.")
        break
    current_location = get_location(name)
    fuel = get_fuel(name)
    print (f"You have arrived to {current_location[1]}")
    travle_again = input(f"Your consumed fuel is {fuel[1]}. Would you like to travle again? [y or n] ")
    if travle_again == "y":
        print("That's fun")
        continue
    else:
        break

# print (change_fuel("Heini"))
# print (airport_distance("Helsinki Vantaa Airport"))
# print (get_fuel("Heini"))
# print (get_location("Heini"))
# print (change_location("London Gatwick Airport", "Heini"))