def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"], start=1):
            print(f"{i}. {choice}")

        user_answer = input("Enter the number of your answer: ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= len(question["choices"]):
                if user_answer == question["correct"]:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Wrong!\n")
            else:
                print("Invalid choice. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")


# Define your quiz questions here as a list of dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct": 3,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Jupiter", "Mercury"],
        "correct": 1,
    },
    {
        "question": "What is the largest mammal on Earth?",
        "choices": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct": 3,
    },
]

# Run the quiz
run_quiz(quiz_questions)
