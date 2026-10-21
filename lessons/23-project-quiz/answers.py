# Practice 2: more than one right answer
# Each question keeps a LIST of right answers, and `in` checks the reply
# against all of them (lesson 18).
questions = [
    {"text": "Name a loop keyword", "answers": ["for", "while"]},
    {"text": "What is 7 // 2?", "answers": ["3", "three"]},
]
score = 0
for n, question in enumerate(questions, start=1):
    print(f"Question {n} of {len(questions)}")
    print(question["text"])
    reply = input("Your answer: ")
    if reply.strip().lower() in question["answers"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Right answers:", ", ".join(question["answers"]))

print(f"You scored {score} out of {len(questions)}")
