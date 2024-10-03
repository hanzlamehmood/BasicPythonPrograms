import random


def guessing_game():
    print("\n" + "=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        print("\nI'm thinking of a number between 1 and 100.")

        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        attempts = 10

        print(f"You have {attempts} attempts to guess the number.")

        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > 100:
                    print("⚠️ Please guess a number between 1 and 100.")
                    continue

                if guess == number_to_guess:
                    print("🎉 Congratulations! You've guessed the correct number!")
                    break
                elif guess < number_to_guess:
                    print("🔽 Too low! Try again.")
                else:
                    print("🔼 Too high! Try again.")

                attempts -= 1
                print(f"You have {attempts} attempts left.")

            except ValueError:
                print("❌ Invalid input! Please enter a number.")

        if attempts == 0:
            print(f"😢 Sorry, you've run out of attempts! The number was {number_to_guess}.")

        # Ask if the player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

guessing_game()
