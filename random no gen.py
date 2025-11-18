import random
import time


def load_leaderboard():
    scores = []
    try:
        with open("leaderboard.txt", "r") as f:
            for line in f:
                name, score, total_time = line.strip().split(",")
                scores.append((name, int(score), float(total_time)))
    except (ValueError, FileNotFoundError):
        pass
    return scores

def show_leaderboard():
    scores = load_leaderboard()
    scores.sort(key=lambda x: x[1], reverse=True)  
    print("LEADERBOARD ")
    for i, (player, score, total_time) in enumerate(scores[:5], start=1):
        print(f"{i}. {player} - {score} pts, {total_time:.2f}s")
   


print("Welcome to the Number Guessing Game!")
while True:  
    name = input("Enter your name: ")
    score = 0

   
    while True:
        print("\nDifficulty Levels:\n1. Easy (1-50)\n2. Hard (1-100)\n3. Impossible (1-500)")
        try:
            difficulty = int(input("Enter your Difficulty (1-3): "))
            if difficulty == 1:
                max_range = 50
                max_attempts = 10
                break
            elif difficulty == 2:
                max_range = 100
                max_attempts = 7
                break
            elif difficulty == 3:
                max_range = 500
                max_attempts = 5
                break
            else:
                print("Please choose a number between 1-3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    
    num = random.randint(1, max_range)
    attempt = 0
    start_time = time.time()  

    print(f"\nGuess a number between 1 and {max_range} in as few attempts as possible!")

    
    while True:
        attempt += 1
        try:
            guess = int(input("Your Guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess > num:
            print("Lower")
            print("Attempts left:", max_attempts - attempt)
        elif guess < num:
            print("Higher")
            print("Attempts left:", max_attempts - attempt)
        else:
            print(f"Correct! The number was {num}")
            print(f"Congratulations! You guessed it in {attempt} attempts.")
            if difficulty == 1:
                score += 500 + 10*(max_attempts - attempt)
            elif difficulty == 2:
                score += 1000 + 20*(max_attempts - attempt)
            else:
                score += 2000 + 50*(max_attempts - attempt)
            break

        if attempt >= max_attempts:
            print(f"Out of attempts! Game Over. The number was {num}")
            break

    
    end_time = time.time()
    total_time = end_time - start_time
    score = round(score)
    with open("leaderboard.txt", "a") as f:
        f.write(f"{name},{score},{total_time}\n")

    print(f"Your score this round: {score} pts, Time: {total_time:.2f}s")

    
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thank you for playing! Goodbye!")
        show_leaderboard()
        break
