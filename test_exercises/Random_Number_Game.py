import random

secret_number = random.randint(1,10) # generate the random number
guess_count = 0 # Count the number of guesse, zero at the beginning of the game

print("Which number I generated between 1 and 10?")
print(f'Take as many guesses as you want. Press "q" if you want to quit the game')

# Use a While True loop to keep the game going indefinitely, until the player quits

while True:
    user_input = (input("Guess the number: "))
    
    # check if the player wants to quit
    if user_input.lower() == 'q':
        print(f"Thanks for playing. The secret number was {secret_number}.")
        break
    
    try:
        guess = int(user_input)
        guess_count += 1
        
        # Use if/elif/else block for comparison
        if guess == secret_number:
            print(f'Correct, you guessed the correct number in {guess_count} tries.')
            break # Exit the loop if the guess is correct
        elif guess > secret_number:
            print(f'Your guess is a bit higher. Try again.')
        else:
            print(f'Your guess is a bit low, try again.')
            
    except ValueError:
        print(f"Invalid input. Please enter a number or 'q' to quit.")