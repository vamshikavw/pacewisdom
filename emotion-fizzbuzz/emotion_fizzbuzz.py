import random

def get_emotion(n):
    if n % 15 == 0:
        return "Surprised"
    elif n % 3 == 0:
        return "Happy"
    elif n % 5 == 0:
        return "Sad"
    else:
        return "Neutral"

def play():
    score = 0
    print("=== Emotion FizzBuzz ===")
    print("div by 3 = Happy | div by 5 = Sad | div by 15 = Surprised | other = Neutral\n")

    while True:
        number = random.randint(1, 99)
        guess = input(f"Number: {number} | Your guess (Happy/Sad/Surprised/Neutral or quit): ").strip().capitalize()

        if guess == "Quit":
            print(f"Game over! Score: {score}")
            break

        correct = get_emotion(number)

        if guess == correct:
            score += 1
            print(f"Correct! Score: {score}\n")
        else:
            print(f"Wrong! It was {correct}. Score: {score}\n")

play()