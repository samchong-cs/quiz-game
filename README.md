# Quiz Game - Malaysia Trivia
# Author : Samuel Chong
# Date started : 13 / 11 / 2025

Goal: A fun, interactive Python quiz game with multiple difficulty levels featuring Malaysia trivia questions.

## Project Timeline:
Day 1 (13/11/2025) : Created trivia questions which were stored in a JSON file as a list with dictionaries inside
Day 2 (15/11/2025) : Created the load, filter, menu and started question display function
Day 3 (16/11/2025) : Touching up code before proceeding further, created score tracking and checking answer function 

## Main bugs I encountered and how they were debugged:
1. 15/11/2025 : Inside filtering difficulty function, I did not assign a variable to the questions and only called the load questions functions, which were not saved to perform tasks later on --> assigned a variable to it
2. 15/11/2025 : User will face a bug if they typed the difficulty with caps --> use .lower() to change the input to automatically match the list
3. 16/11/2025 : Mistake of using global for questions variable which was not needed --> removed it because there is no shared variable to modify

## Features
- Multiple difficulty levels (easy, medium, hard)
- JSON-based question storage
- Score tracking
- Replay option
- Malaysia-themed questions

## How to Run
1. Clone the repository
2. Run: python quiz_game.py
3. Follow the menu prompts

## Technologies Used
- Python 3.8.7
- JSON for data storage
