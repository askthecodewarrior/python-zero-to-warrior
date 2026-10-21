# Your turn: a question of your own, and a perfect score
# This is quiz.py from the video.
# TODO 1: add a fourth question to the list (above the closing bracket),
#         with its answer in lowercase, in quotes. Then run it: it says
#         "Question 1 of 4" and "out of 4" with no other changes.
# TODO 2: after the last line, add an if: when score == len(questions),
#         print("Perfect score!")

# 1. The questions and their answers
questions = [
    {"text": "What type is 3.5?", "answer": "float"},
    {"text": "What is 7 // 2?", "answer": "3"},
    {"text": "What keyword ends a loop?", "answer": "break"},
]
print(f"Python quiz: {len(questions)} questions")

# 2. Ask each question and check the reply
score = 0
for n, question in enumerate(questions, start=1):
    print(f"Question {n} of {len(questions)}")
    print(question["text"])
    reply = input("Your answer: ")
    if reply.strip().lower() == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer was", question["answer"])

# 3. Show the final score
print(f"You scored {score} out of {len(questions)}")
