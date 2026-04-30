print("Welcome to Python Quiz!")
score = 0

print("\nQ1: What is 2 + 2?")
print("a) 3\nb) 4\nc) 5")

answer = input("Your answer: ")

if answer == "b":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nFinal Score:", score)
