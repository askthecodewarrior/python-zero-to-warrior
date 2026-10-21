# Practice 3: a second try before the answer is shown
questions = [
    {"text": "What type is 3.5?", "answer": "float"},
    {"text": "What is 7 // 2?", "answer": "3"},
    {"text": "What keyword ends a loop?", "answer": "break"},
]
score = 0
for n, question in enumerate(questions, start=1):
    print(f"Question {n} of {len(questions)}")
    print(question["text"])
    reply = input("Your answer: ")
    if reply.strip().lower() == question["answer"]:
        print("Correct!")
        score += 1
    else:
        reply = input("Not quite. Try once more: ")
        if reply.strip().lower() == question["answer"]:
            print("Correct on the second try!")
            score += 1
        else:
            print("Wrong! The answer was", question["answer"])

print(f"You scored {score} out of {len(questions)}")
