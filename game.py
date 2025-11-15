# Started : 13 Nov 2025
# Author  : Samuel Chong

global questions

import json
import os

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

questions = load_questions()
filter_difficulty(questions, "medium")