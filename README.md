# Quiz Game - Malaysia Trivia
# Author : Samuel Chong
# Date started : 13 / 11 / 2025

Goal: A fun, interactive Python quiz game with multiple difficulty levels featuring Malaysia trivia questions.

## Project Timeline:
Day 1 (13/11/2025) : Created trivia questions which were stored in a JSON file as a list with dictionaries inside
Day 2 (15/11/2025) : Created the load, filter, menu and started question display function
Day 3 (16/11/2025) : Touching up code before proceeding further, created score tracking and checking answer function
Day 4 (17/11/2025) : Wrapping up project with play_game function and creating loop for user to play again

## Main bugs I encountered and how they were debugged:
1. 15/11/2025 : Inside filtering difficulty function, I did not assign a variable to the questions and only called the load questions functions, which were not saved to perform tasks later on --> assigned a variable to it
2. 15/11/2025 : User will face a bug if they typed the difficulty with caps --> use .lower() to change the input to automatically match the list
3. 16/11/2025 : Mistake of using global for questions variable which was not needed --> removed it because there is no shared variable to modify
4. 17/11/2025 : Getting the is_correct variable wrong --> sticked with the paramaters of the original function
5. 17/11/2025 : return statement indentation was wrong --> placed the statement outside of the loop
6. 17/11/2025 : calling check answer twice -->  changed to one time
7. 17/11/2025 : did not use .lower() for user input for playing again
8. 17/11/2025 : did not add parameter when calling play_game function --> added the parameter "selected questions"

## Project Structure Summary:
1. load_questions() : this function loads the questions from the questions json file and saves the questions into a variable called 'questions'
2. filter_difficulty() : this function creates a loop in the list of questions and it adds each question dictionary from the questions.json file into the list based on the difficulty the user enters when it is called in the menu function later
3. menu(): this function asks the user to select the difficulty of the questions they want and store it in a vairable which is needed when calling the filter difficulty function
4. display_question() : prints the questions and options neatly and saves the user answer as variable to be used later
5. check_answer() : returns True or False based on whether user answer is correct
6. track_score() : checks whether the user answer was correct then adds one to the score if it was
7. play_game() : sets score variable to be zero and then basically just combining most of the other functions to actually play the game
8. Loop at the end : created so that users can play again depending on what they type and also to call functions

## Key things I learned:
1. How to handle JSON files
2. Understanding how lists work more - more Pythonic way to filter data in one line
3. When to use parameters vs global variables
4. How functions can work together

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
