import random

def algebra_practice_game():
    score = 0
    rounds=int(input("Enter the number of questions you want to solve:"))
     # Number of rounds to play

    for _ in range(rounds):
        problem_type = random.choice(["one-step", "two-step"])

        if problem_type == "one-step":
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            answer = a + b
            print(f"Solve: {a} + {b} = ?")

        elif problem_type == "two-step":
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            answer = a * b + c
            print(f"Solve: {a} * {b} + {c} = ?")

        user_answer = int(input("Your answer: "))
        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was {answer}.")

    print(f"Your score: {score}/{rounds}")

# Run the game
algebra_practice_game()
