# Started : 13 Nov 2025
# Author  : Samuel Chong

global questions

import json

def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    return questions

def filter_difficulty(questions, difficulty):
    filtered = []
    for question in questions:
        if question["difficulty"] == difficulty:
            filtered.append(question)
    return filtered

def menu():
    print("\nYou can choose from the following difficulty options: \n 1) Easy 😄 \n 2) Medium 😐 \n 3) Hard 😈")
    user_difficulty_choice = input("\nType the difficulty level you want for the quiz: ").lower()
    filtered_questions = filter_difficulty(questions, user_difficulty_choice)
    return filtered_questions 

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer: ")
    return user_answer

questions = load_questions()
selected_questions = menu()

if selected_questions:
    user_answer = display_question(selected_questions[0])
    print(f"You answered: {user_answer}")