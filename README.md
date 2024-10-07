# Python Software Project: Flight Simulator Game ✈️

## Overview
Welcome to the **Flight Simulator Game**! This is a console-based game where players simulate traveling between airports while progressing through various levels of difficulty. The game allows players to manage locations, participate in interactive challenges, and see how far they can travel.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Game Phases](#game-phases)
- [Game Rules](#game-rules)
- [How to Play](#how-to-play)
- [Database Setup](#database-setup)

## Features
- **Player Registration**: Register with a unique screen name or log in to an existing one.
- **Location Management**: Travel between various airports across levels.
- **Level Progression**: Unlock harder levels as you keep playing.
- **Arrow Key Challenges**: Complete quick-tap challenges to earn points.
- **Random Events**: Encounter random events that add excitement to the journey.
- **Scoreboard**: Track and view players' scores.

## Requirements
To run this game, ensure the following are installed:
- Python 3.x
- `keyboard` library

## Game Phases
The game progresses through the following phases:

Player Registration: Enter your screen name to register or log in.

Select Destination: Choose an airport to travel to.

Complete Challenges: Respond to prompts like pressing arrow keys.

Random Events: Face random events that influence the game.

Level Up: As you succeed, move to higher difficulty levels.


## Game Rules

1. Register as a new player or continue an existing game.
2. Choose a destination airport and complete the journey by passing the challenges.
3. Earn points by successfully completing arrow key challenges.
4. Progress to higher levels as you keep playing.

## How to Play

1. Start the Game: Run the lentosimulaattori.py script.
2. Register/Log In: Enter your name to start the game.
3. Select Destination: Choose the airport you want to travel to.
4. Complete Challenges: React to arrow key prompts within the time limit.
5. Progress: Keep playing to level up and encounter more difficult challenges.

## Files Overview
Here are the key files that make up the game:
1. lentosimulaattori.py: The main file to run the game. This handles player interactions, including registration, selecting destinations, and calling functions from other files.
2. funktiot.py: Contains core game logic and utility functions like managing locations and handling challenges.
3. taso_funktiot.py: Handles level progression and random events. This file manages how the game becomes more difficult as the player advances.

## Database Setup
Ainoat muutokset, jotka olemme tehneet tietokantaan:

INSERT INTO game (points) VALUES (0);
INSERT INTO game (points) VALUES (0);
