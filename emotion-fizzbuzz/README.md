# Emotion FizzBuzz Game

A simple command-line guessing game built using Python, demonstrating the use of **functions**, **loops**, and **conditionals**.

## About

Emotion FizzBuzz is inspired by the classic FizzBuzz problem. Instead of printing Fizz or Buzz, each number is assigned an emotion based on its divisibility. A random number is shown each round and the player must guess the correct emotion.

## Emotion Rules

| Condition         | Emotion    |
|-------------------|------------|
| Divisible by 15   | Surprised  |
| Divisible by 3    | Happy      |
| Divisible by 5    | Sad        |
| Any other number  | Neutral    |

## Concepts Used

- **Functions** — `get_emotion(n)` returns the emotion for a given number. `play()` runs the game loop.
- **Conditionals** — `if/elif/else` checks divisibility inside `get_emotion()` and validates the player's guess.
- **Loops** — `while True` keeps the game running until the player types `quit`.

## How to Run

```bash
python emotion_fizzbuzz.py
```

## Sample Output

```
=== Emotion FizzBuzz ===
div by 3 = Happy | div by 5 = Sad | div by 15 = Surprised | other = Neutral

Number: 9 | Your guess (Happy/Sad/Surprised/Neutral or quit): Happy
Correct! Score: 1

Number: 25 | Your guess (Happy/Sad/Surprised/Neutral or quit): Sad
Correct! Score: 2

Number: 30 | Your guess (Happy/Sad/Surprised/Neutral or quit): Happy
Wrong! It was Surprised. Score: 2
```

## Files

| File                   | Description              |
|------------------------|--------------------------|
| `emotion_fizzbuzz.py`  | Main game code           |
| `README.md`            | Project documentation    |
