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
        print("Well come back!")
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

    return (f"Player {name}'s location has been updated to {destination}")

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

    print(f"Calculated distance from {airport1} to {airport2} is {distance:.2f} km.")

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
    print(result)

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

while True:
    name = input("What is your name? ")
    add_player(name)
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


# By Hussein -----------------------------------------------------------------------------------By Hussein#


import mysql.connector
from datetime import datetime
import random

# By Hussein -----------------------------------------------------------------------------------By Hussein#
# Function to connect to the database
def connect_to_database():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='hussein',  # Database username
            password='kesko11@@',  # Database password
            database='flight_game',
            charset="utf8mb4",
            collation="utf8mb4_general_ci",
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to get a valid integer input

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to get a valid date

def get_valid_date(prompt):
    today = datetime.today().date()
    while True:
        date_str = input(prompt)
        try:
            date = datetime.strptime(date_str.replace("-", "/"), '%d/%m/%Y').date()
            if date < today:
                print("Date cannot be in the past. Please enter a future date.")
            else:
                return date
        except ValueError:
            print("Invalid date format. Please enter DD/MM/YYYY or DD-MM-YYYY.")

# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to get valid trip type

def get_valid_trip_type():
    valid_types = ['one-way', 'two-way']
    while (trip_type := input("Is this a one-way or two-way trip? (one-way/two-way): ").lower()) not in valid_types:
        print("Invalid trip type. Please enter 'one-way' or 'two-way'.")
    return trip_type

# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to get valid IATA code

def get_valid_iata_code(prompt):
    while True:
        iata_code = input(prompt).strip().upper()
        if len(iata_code) == 3 and iata_code.isalpha():
            return iata_code
        print("Invalid IATA code. Please enter a valid 3-letter IATA code.")

# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to get class type (VIP or Economy)

def get_class_type():
    while (class_type := input("Do you want to book VIP class or Economy class? (VIP/Economy): ").strip().lower()) not in ['vip', 'economy']:
        print("Invalid input. Please enter 'VIP' or 'Economy'.")
    return class_type

# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to check baggage allowance and costs

def check_baggage(class_type):
    if class_type == 'economy':
        if input("Do you want to add extra baggage (more than 12 kg up to 50 kg) for €35? (yes/no): ").strip().lower() == 'yes':
            print("Extra baggage added for €35. Total allowance is 50 kg.")
            return 35  # Extra baggage cost
        print("You are entitled to 12 kg of baggage only.")
    else:
        print("You are entitled to 50 kg of baggage.")
    return 0  # No cost for VIP class

# By Hussein -----------------------------------------------------------------------------------By Hussein#

# Function to book flight

def book_flight(conn):
    cursor = conn.cursor()

    # Get number of adults and children
    num_adults = get_valid_int("Enter number of adults: ")
    num_children = get_valid_int("Enter number of children: ")
    
    passengers = []
    total_baggage_cost = 0
    
    for i in range(num_adults + num_children):
        first_name = input(f"Enter first name of passenger {i + 1}: ")
        last_name = input(f"Enter last name of passenger {i + 1}: ")
        age = get_valid_int(f"Enter age of passenger {i + 1}: ")
        class_type = get_class_type()
        
        baggage_cost = check_baggage(class_type)
        total_baggage_cost += baggage_cost

        passengers.append((first_name, last_name, age, class_type))

    # Get IATA codes
    start_location = get_valid_iata_code("Enter start airport IATA code: ")
    destination = get_valid_iata_code("Enter destination airport IATA code: ")
    
    # Get and validate the departure date
    departure_date = get_valid_date("Enter departure date (DD/MM/YYYY or DD-MM-YYYY): ")
    
    # Get trip type
    trip_type = get_valid_trip_type()
    
    # Calculate prices
    adult_price = random.randint(400, 800) if passengers[0][3] == 'vip' else random.randint(200, 500)
    child_price = adult_price * 0.5  # Children's price
    total_cost = (num_adults * adult_price) + (num_children * child_price) + total_baggage_cost

    return_date = None

    
    if trip_type == 'two-way':
        while True:
            return_date = get_valid_date("Enter return date (DD/MM/YYYY or DD-MM-YYYY): ")
            if return_date >= departure_date:
                break
            print("Return date cannot be before departure date.")
        total_cost *= 1.1  # 10% extra for round trip

    # Print booking summary
    print("\nBooking Summary:")
    for first_name, last_name, age, class_type in passengers:
        print(f"Passenger: {first_name} {last_name}, Age: {age}, Class: {class_type.capitalize()}")
    
    print(f"From: {start_location} to {destination}, Departure: {departure_date}, Return: {return_date if return_date else 'N/A'}")
    print(f"Total Adults: {num_adults}, Total Children: {num_children}, Total Cost: €{total_cost:.2f} (Adult: €{adult_price}, Child: €{child_price}, Baggage: €{total_baggage_cost})")

    # Confirm booking
    if input("Confirm this booking? (yes/no): ").strip().lower() == 'yes':
        cursor.execute(
            "INSERT INTO bookings (start_location, destination, total_cost, departure_date) VALUES (%s, %s, %s, %s)",
            (start_location, destination, total_cost, departure_date)
        )
        conn.commit()
        print("Booking confirmed successfully!")
    else:
        print("Booking cancelled.")

    cursor.close()

# Main function
def main():
    conn = connect_to_database()
    if conn:
        book_flight(conn)
        conn.close()

if __name__ == "__main__":
    main()  # Run the main function
