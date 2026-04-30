questions = [
    "What is 2 + 2?",
    "What is 5 * 2?",
    "What is 10 / 2?",
    "What is 3 + 3?"
]

options = [
    "a) 3  b) 4  c) 5",
    "a) 10  b) 7  c) 12",
    "a) 2  b) 5  c) 10",
    "a) 5  b) 6  c) 7"
]

answers = ["b", "a", "b", "b"]

score = 0

for i in range(len(questions)):
    print("\n", questions[i])
    print(options[i])

    answer = input("Your answer: ")

    if answer == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

print("\nFinal Score:", score, "/", len(questions))
