import random


def get_computer_choice():
    """Randomly choose between Rock, Paper, or Scissors for the computer."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the choices."""
    if player_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win! 🎉"
    else:
        return "You lose! 😢"


def play_game():
    print("\n" + "=" * 40)
    print("   Welcome to Rock, Paper, Scissors!")
    print("=" * 40)

    while True:
        rounds = int(input("How many rounds would you like to play? "))
        player_score = 0
        computer_score = 0

        for round_num in range(1, rounds + 1):
            print(f"\n--- Round {round_num} ---")
            player_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
            while player_choice not in ["Rock", "Paper", "Scissors"]:
                print("Invalid choice! Please try again.")
                player_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(player_choice, computer_choice)
            print(result)

            if "win" in result:
                player_score += 1
            elif "lose" in result:
                computer_score += 1

            print(f"Score: You {player_score} - Computer {computer_score}")

        print("\nGame over!")
        if player_score > computer_score:
            print("You are the overall winner! 🏆")
        elif player_score < computer_score:
            print("Computer is the overall winner! 🤖")
        else:
            print("It's an overall tie! 🎊")

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()

