import mysql.connector
from geopy.distance import geodesic
from random import randint, sample
import time
import os

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='hussein',
    password='kesko11@@',
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
        print("Welcome back!")
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

# New: Define questions for Level 1
# Done BY Omar
level_1_questions = [
    {
        "question": "⚠️ You’ve encountered a storm mid-flight! Make the right decision to pass safely.",
        "options": ["1. Fly above the storm.", "2. Fly directly through the storm.", "3. Attempt a dangerous emergency landing in the ocean."],
        "correct": 1
    },
    {
        "question": "🌪️ Alert: You are entering a turbulent zone! Choose your action carefully.",
        "options": ["1. Dive down to a lower altitude to escape the turbulence.", "2. Maintain your current altitude and ride it out.", "3. Ascend to a higher altitude to avoid the turbulence."],
        "correct": 3
    },
    {
        "question": "🔧 Alert: You’ve experienced a mechanical failure! Decide how to respond.",
        "options": ["1. Try to land the plane immediately", "2. Check the instruments to assess the damage.", "3. Call for emergency assistance while flying level."],
        "correct": 2
    }
]

# New: Define questions for Level 2
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
level_2_questions = [
    {
        "question": "🛩️ You're flying over a mountainous region. Suddenly, you spot a potential obstacle ahead!",
        "options": ["1. Steer left to avoid the obstacle.", "2. Steer right and risk getting closer to the mountains.", "3. Ascend and hope to fly over it."],
        "correct": 3
    },
    {
        "question": "⚡ You receive a warning about an incoming air traffic conflict!",
        "options": ["1. Immediately change your altitude.", "2. Ignore the warning and maintain your course.", "3. Contact air traffic control for guidance."],
        "correct": 1
    },
    {
        "question": "🛬 You are preparing for landing, but weather conditions are deteriorating!",
        "options": ["1. Attempt to land immediately despite the weather.", "2. Circle around and wait for conditions to improve.", "3. Divert to the nearest airport."],
        "correct": 3
    }
]

# New: Define questions for Level 3
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
level_3_questions = [
    {
        "question": "🚀 You're approaching a spaceport for landing. Choose your approach strategy!",
        "options": ["1. Use a steep descent for a quick landing.", "2. Approach at a normal angle.", "3. Circle around to wait for landing clearance."],
        "correct": 2
    },
    {
        "question": "🛰️ Suddenly, you lose contact with ground control! What will you do?",
        "options": ["1. Keep flying and hope for the best.", "2. Attempt to re-establish contact.", "3. Land at the nearest airstrip."],
        "correct": 2
    },
    {
        "question": "🌌 You encounter unexpected cosmic debris on your path!",
        "options": ["1. Try to dodge the debris.", "2. Increase speed to pass through quickly.", "3. Change course to avoid any collision."],
        "correct": 3
    }
]

# New: Define questions for Level 4
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
level_4_questions = [
    {
        "question": "🏁 You're on the final approach to a busy airport. Choose your landing gear strategy!",
        "options": ["1. Deploy landing gear early for safety.", "2. Wait until the last moment to deploy landing gear.", "3. Circle for another approach."],
        "correct": 1
    },
    {
        "question": "💡 You notice a warning light for low fuel! What's your response?",
        "options": ["1. Ignore the warning and continue.", "2. Find the nearest airport to land.", "3. Try to conserve fuel by flying lower."],
        "correct": 2
    },
    {
        "question": "🚧 Air traffic is heavy. What will you do?",
        "options": ["1. Request priority landing.", "2. Wait for your turn.", "3. Attempt to land without clearance."],
        "correct": 2
    }
]

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
    return 

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
    return distance

# Done by Omar
def change_fuel(name, destination):
    distance = airport_distance(name, destination)
    fuel_consumed = (distance / 100) * 10
    sql =   f"""  update game
                set co2_budget = (co2_budget - {fuel_consumed}),
                co2_consumed = (co2_consumed + {fuel_consumed})
                where screen_name = %s;"""
    
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()
    return 

# Main Game Loop
# Done by Omar
while True:
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
    print('Welcome to the Pilot game')
    print("The basis of the game is based on the assumption that you are a pilot and you face some difficulties during your journey")
    print("The Game starts...")
# Done by Omar
    name = input("Hello Commander what is your name? ")
    while True:
        add_player(name)
        current_location = get_location(name)
        points = get_points(name)
        fuel = get_fuel(name)
        destination = input(f"You're currently at {current_location[1]} with a fuel budget of {fuel[0]}. Where would you like to fly next? ")
        make_sure = input(f"Fuel usage: {fuel[1]} units. Do you want to keep going? (Y/N): ")
        
        if make_sure.upper() == "Y":
            # airplane_shape()  # Assuming you have a function for airplane shape, it is commented out

            total_correct_answers = 0  # Initialize total correct answers for summary
# Done by Omar
            # Level 1
            correct_answers_level_1 = 0
            questions_level_1 = sample(level_1_questions, 3)
            for q in questions_level_1:
                print(q["question"])
                for option in q["options"]:
                    print(option)
                choice = int(input("Choose 1, 2 or 3: "))
                if choice == q["correct"]:
                    print("✅ Correct choice!")
                    correct_answers_level_1 += 1
                    change_points(name)
                else:
                    print("❌ Wrong choice! Here's the correct answer:")
                    print(f"Correct Answer: {q['options'][q['correct'] - 1]}")  # Display correct option
                    break  # Exit loop on wrong answer
            else:  # This else corresponds to the for loop
                total_correct_answers += correct_answers_level_1  # Add to total if loop was not broken
                if correct_answers_level_1 < 2:
                    print("You need to answer at least 2 questions correctly to proceed to Level 2.")
                    default_settings(name)
                    continue  # Restart the loop
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
                # Level 2
                correct_answers_level_2 = 0
                questions_level_2 = sample(level_2_questions, 3)
                for q in questions_level_2:
                    print(q["question"])
                    for option in q["options"]:
                        print(option)
                    choice = int(input("Choose 1, 2 or 3: "))
                    if choice == q["correct"]:
                        print("✅ Correct choice!")
                        correct_answers_level_2 += 1
                        change_points(name)
                    else:
                        print("❌ Wrong choice! Here's the correct answer:")
                        print(f"Correct Answer: {q['options'][q['correct'] - 1]}")  # Display correct option
                        break
                else:  # This else corresponds to the for loop
                    total_correct_answers += correct_answers_level_2  # Add to total if loop was not broken
                    if correct_answers_level_2 < 2:
                        print("You need to answer at least 2 questions correctly to proceed to Level 3.")
                        default_settings(name)
                        continue  # Restart the loop
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
                    # Level 3
                    correct_answers_level_3 = 0
                    questions_level_3 = sample(level_3_questions, 3)
                    for q in questions_level_3:
                        print(q["question"])
                        for option in q["options"]:
                            print(option)
                        choice = int(input("Choose 1, 2 or 3: "))
                        if choice == q["correct"]:
                            print("✅ Correct choice!")
                            correct_answers_level_3 += 1
                            change_points(name)
                        else:
                            print("❌ Wrong choice! Here's the correct answer:")
                            print(f"Correct Answer: {q['options'][q['correct'] - 1]}")  # Display correct option
                            break
                    else:  # This else corresponds to the for loop
                        total_correct_answers += correct_answers_level_3  # Add to total if loop was not broken
                        if correct_answers_level_3 < 2:
                            print("You need to answer at least 2 questions correctly to proceed to Level 4.")
                            default_settings(name)
                            continue  # Restart the loop
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
                        # Level 4
                        correct_answers_level_4 = 0
                        questions_level_4 = sample(level_4_questions, 3)
                        for q in questions_level_4:
                            print(q["question"])
                            for option in q["options"]:
                                print(option)
                            choice = int(input("Choose 1, 2 or 3: "))
                            if choice == q["correct"]:
                                print("✅ Correct choice!")
                                correct_answers_level_4 += 1
                                change_points(name)
                            else:
                                print("❌Wrong choice! Here's the correct answer:")
                                print(f"Correct Answer: {q['options'][q['correct'] - 1]}")  # Display correct option
                                break
                        else:  # This else corresponds to the for loop
                            total_correct_answers += correct_answers_level_4  # Add to total if loop was not broken
                            change_fuel(name, destination)
                            change_location(destination, name)
# Done BY Hussein ----------------------------------------------------------------------------------------------Done By Hussein
            # Summary of performance
            total_questions = 12  # Total questions across all levels
            if total_correct_answers > 0:  # Display summary if at least one question was answered correctly
                success_rate = (total_correct_answers / total_questions) * 100
                points = get_points(name)
                current_location = get_location(name)
                fuel = get_fuel(name)
                print(f"Welcome! You've just arrived at {current_location[1]}!")
                print(f"Congratulations! You've earned a point. Your total points are now {points}.")
                print(f"Summary for {name}:")
                print(f"Total Correct Answers: {total_correct_answers}/{total_questions}")
                print(f"Success Rate: {success_rate:.2f}%")
            else:
                print("You did not answer any questions correctly. Please try again!")
# Done by Omar
            # Ask to play again
            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.upper() != "N":
                print("Welcome Again")
                default_settings(name)
            break  # Exit the main game loop
        else:
            print("No worries! Until next time!")
            default_settings(name)
        break  # Exit the main game loop
