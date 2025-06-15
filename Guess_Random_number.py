import random

def main():
    while True:
        random_number = random.randint(1, 100)
        guess_count = 0
        correct_guess = False
        
        print("I have generated a random number between 1 and 100. Try to guess it!")
        
        while not correct_guess:
            guess = int(input("Enter your guess: "))
            guess_count += 1
            if guess > random_number:
                print("Too high, try again.")
            elif guess < random_number:
                print("Too low, try again.")
            else:
                print(f"Congratulations! You guessed the number in {guess_count} tries.")
                correct_guess = True

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()