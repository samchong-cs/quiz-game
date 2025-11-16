# Started : 13 Nov 2025
# Author  : Samuel Chong

import json

def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    return questions

def filter_difficulty(questions, difficulty):
    filtered = [question for question in questions if question["difficulty"] == difficulty]

    return filtered

def menu(questions):
    print("\nYou can choose from the following difficulty options: \n 1) Easy 😄 \n 2) Medium 😐 \n 3) Hard 😈")
    user_difficulty_choice = input("\nType the difficulty level you want for the quiz: ").lower()

    filtered_questions = filter_difficulty(questions, user_difficulty_choice)

    return filtered_questions 

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

    answer = input("Enter your answer: ")
    return answer

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def track_score(is_correct, score):
    if is_correct:
        score += 1
    return score

questions = load_questions()
selected_questions = menu(questions)

# Question runs here after menu function filters:
if selected_questions:
    global user_answer
    user_answer = display_question(selected_questions[0])
    print(f"You answered: {user_answer}")
