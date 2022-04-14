def main():
    from guessing_logo import logo
    import random

    EASY_TURNS = 10
    HARD_TURNS = 5
    
    # Check if the player guess matches the random number, if not then subtract 1 from their turns
    def check_guess(p_guess, ran_number, turns):
        if p_guess == ran_number:
            print(f'\nYou got it! The number was {p_guess}! You win!')
        elif p_guess > ran_number:
            print('\nYour guess is too high!')
            return turns - 1
        else:
            print('\nYour guess is too low!')
            return turns - 1

    # Ask the user for a difficulty level, if they choose easy give them 10 turns, if not give them 5 turns
    def choose_difficulty():
        difficulty = input('\nChoose your difficulty: easy (10 turns) or hard (5 turns)? ')
        
        if difficulty == 'easy' or difficulty == 'Easy' or difficulty == 'EASY':
            return EASY_TURNS
        else:
            return HARD_TURNS

    def guess_number():
        print(logo)
        print("\nWelcome! Let's play a game of Guess the Number!")
        print(f"\nRight now I'm thinking of a number between 1 and 100, can you figure it out?.\n")
        
        # Generate a number between 1 and 100 for our game
        ran_number = random.randint(1, 100)
        
        # Call choose_difficulty to ask the user for a difficulty level
        turns = choose_difficulty()
        
        p_guess = 0
        
        # Keep playing while the player guess isn't correct
        while p_guess != ran_number:
            print(f'\nYou have {turns} turns left to figure out the number.')
            
            p_guess = int(input("\nWhat's your guess?: "))
            
            # Call check_guess to see if the player guessed correctly
            turns = check_guess(p_guess, ran_number, turns)
            
            # If the player runs out of turns then end the game
            if turns == 0:
                print(f'\nWhoops! You ran out of turns! You lose! The number was: {ran_number}')
                return
            elif p_guess != ran_number:
                print("\nSorry, that's not it!")

    guess_number()

if __name__ == "__main__":
    main()