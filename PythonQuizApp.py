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

while True:

    score = 0

    print("\n🎮 Welcome to Python Quiz Game!\n")

    for i in range(len(questions)):
        print("Q" + str(i + 1) + ":", questions[i])
        print(options[i])

        answer = input("Your answer (a/b/c): ").lower().strip()

        if answer == answers[i]:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!\n")

    print("🏁 Final Score:", score, "/", len(questions))

    if score == len(questions):
        print("🔥 Perfect score!")
    elif score >= len(questions) / 2:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")

    again = input("\nDo you want to play again? (y/n): ").lower().strip()

    if again == "n":
        print("👋 Thanks for playing!")
        break
