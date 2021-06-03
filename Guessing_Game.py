secret_number = 10
No_of_guesses = 0
No_of_guess_limit = 3
while  No_of_guesses < No_of_guess_limit:
    guess=int(input('Guess: '))
    No_of_guesses += 1
    if guess == secret_number:
        print("You won.")
        break
else:
    print("You lost.")
