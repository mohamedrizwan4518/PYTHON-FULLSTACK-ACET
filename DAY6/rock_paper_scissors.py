import random

def play(user_score=0, comp_score=0):
    choices = ["rock", "paper", "scissors"]

    print("\n--- Rock Paper Scissors ---")
    user = input("Choose rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        return play(user_score, comp_score)  # recursion for invalid input

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    # Game logic
    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        comp_score += 1

    print(f"Score -> You: {user_score} | Computer: {comp_score}")

    again = input("Play again? (y/n): ").lower()

    if again == "y":
        return play(user_score, comp_score)  # recursion keeps score
    else:
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {comp_score}")
        print("Thanks for playing!")


play()
