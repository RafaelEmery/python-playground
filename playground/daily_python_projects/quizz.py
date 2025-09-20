"""
Your task for today is to build an interactive quiz game using Python classes and a Gradio web interface. 
This project teaches how to design a system with multiple interconnected classes and wrap it into a user-friendly web app.

Core Classes
    Question(text: str, options: list[str], answer: int)
        Represents one question. Stores the text, a list of options, and the index of the correct answer.
    Quiz(questions: list[Question])
        Manages the flow of the game.

Methods:
    next_question() → returns the current Question object
    submit(choice: int) → checks answer, updates score, advances to next
    reset() → resets all progress and score
    summary() → returns final score, accuracy, and time taken

Example Usage:
questions = [
    Question("What is the capital of France?", ["Paris", "London", "Berlin"], 0),
    Question("Which language is this quiz written in?", ["Java", "Python", "C++"], 1),
    Question("2 + 2 = ?", ["3", "4", "5"], 1),
    Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Saturn"], 1),
    Question("Which year did World War II end?", ["1944", "1945", "1946"], 1)
]
"""