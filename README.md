# Python_Software1_Project

Welcome to the Flight Game! This is an interactive console-based game where players can simulate traveling between airports while managing fuel consumption. The game tracks players' locations and fuel budgets, providing a fun way to learn about aviation and geography.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Game Phases](#game-phases)
- [Game Rules](#game-rules)
- [How to Play](#how-to-play)
- [Functions Overview](#functions-overview)

## Features

- **Player Registration**: Register with a unique screen name.
- **Location Management**: Change your location by traveling to different airports.
- **Fuel Consumption Tracking**: Monitor your fuel budget and consumption based on travel distance.
- **Distance Calculation**: Calculate the distance between airports using geographical coordinates.
- **Interactive Gameplay**: Engage in a loop where you can travel multiple times until you decide to quit.
- **Scoreboard**: View a scoreboard of all players and their points.
- **Random Events**: Encounter random events during flights that can affect your journey.
- **Level Progression**: Progress through multiple levels with increasing difficulty.
- **Arrow Key Challenges**: Complete challenges by pressing arrow keys quickly to earn points.

## Requirements

To run this game, ensure you have the following installed:

- Python 3.x
- MySQL Connector for Python
- Geopy library


## Game Phases
The game progresses through the following phases:

Player Registration:

Players enter their screen name. If the name is already registered, they are welcomed back.
Current Location and Fuel Status:

Players are informed of their current airport location and fuel budget. The game retrieves this information from the database.
Destination Input:

Players choose their destination airport. They can input the name of an airport they wish to travel to.
Fuel Confirmation:

The game calculates the consumed fuel based on the distance to the destination and asks for confirmation to proceed with the travel.
Travel Execution:

If the player confirms, the game updates their fuel consumption and changes their location to the new airport. It displays an ASCII representation of an airplane during the transition.
Post-Travel Update:

Players are informed of their new location and current fuel status. They can choose to travel again or exit the game.


## Game Rules

When prompted, enter your screen name to register or to return to the game.
The game will display your current airport location and available fuel budget.
Enter your desired destination airport. If your fuel budget allows, confirm to proceed with the travel.
The game will calculate the distance traveled and update your fuel consumption.
You can choose to travel again or exit the game.

## How to Play

1. **Start the Game**: Run the `Flight_simulator.py` script.
2. **Enter Your Name**: Input your screen name to register or continue.
3. **View Scoreboard**: Choose whether to view the scoreboard of all players.
4. **Select Destination**: Choose your next destination by entering the country code and airport ID.
5. **Manage Fuel**: Monitor your fuel consumption and ensure you have enough to reach your destination.
6. **Complete Challenges**: Press arrow keys quickly when prompted to earn points.
7. **Encounter Random Events**: Make decisions during random events to continue your journey.
8. **Progress Through Levels**: Successfully complete levels to progress to more challenging ones.
9. **Win the Game**: Accumulate points and complete all levels to win the game.

- player_exists(name): Checks if a player already exists in the database.

- get_count_of_players(): Returns the total number of players registered.

- add_player(name): Adds a new player or welcomes back an existing player.

- get_location(name): Retrieves the current location of the player.

- change_location(destination, name): Updates the player's location to a new destination.

- get_fuel(name): Returns the current fuel budget and consumed fuel of the player.

- airport_distance(name, destination): Calculates the distance between the current airport and the destination airport.

- change_fuel(name, destination): Updates the fuel consumption based on the distance traveled.

- airplane_shape(): Displays a simple ASCII art representation of an airplane.
