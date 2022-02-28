def main():

    from blackjack_logo import logo
    import random
    import os

    # Deals a random card from the deck (deck is infinite for simplicity's sake)
    def deal_card():
        deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        dealed_card = random.choice(deck_cards)
        return dealed_card

    def calculate_score(cards):
        score = sum(cards)
        if score == 21 and len(cards) == 2:
            # Return a blackjack
            return 0
        # In blackjack you can choose if your ace is worth 1 or 11, so if the user has an ace and the score is greater than 21 (maximum score for a blackjack) we change the ace to 1
        elif 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
            return score
        else:
            # Return the cards sum score
            return score

    # Compare the scores and print the winner depending on the result
    def compare_scores(user_score, house_score):
        if user_score == house_score or (user_score == 0 and house_score == 21):
            return "\nIt's a draw!"
        elif house_score == 21:
            return '\nThe house got a blackjack! You lose!'
        elif user_score == 0:
            return '\nYou got a blackjack! You win!'
        elif  user_score > 21:
            return '\nYou busted! You lose!'
        elif house_score > 21:
            return '\nThe house busted! You win!'
        elif user_score > house_score:
            return '\nYour score was higher! You win!'
        else:
            return '\nYour score was lower! You lose!'

    def blackjack():

        print(logo)
        
        game_ended = False
        user_cards = []
        house_cards = []
        
        # Deal 2 cards to the user and the house
        for _ in range(2):
            user_cards.append(deal_card())
            house_cards.append(deal_card())

        print(f'\nYour cards: {user_cards}, Your current score: {calculate_score(user_cards)}')
        # In blackjack the house always starts with the first card hidden
        print(f'\nHouse cards: [#, {house_cards[1]}]')
        
        # Keep the game going until the user is done
        while not game_ended:

            # Calculate both scores
            user_score = calculate_score(user_cards)
            house_score = calculate_score(house_cards)
            
            print('\nRemember: If your current score shows as 0, you have a blackjack!')
            
            user_answer = input("\nWould you like to draw another card? (y/n): ")

            # If the users wants to hit, add a card to the user's cards and update the score
            while user_answer == "y" and user_score < 21:
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f'\nYour cards: {user_cards}, Your current score: {calculate_score(user_cards)}')
                # In blackjack the house always starts with the first card hidden
                print(f'\nHouse cards: [#, {house_cards[1]}]')
                user_answer = input("\nWould you like to draw another card? (y/n): ")
            else:
                pass
            
            # If the house's score is less than 17, add a card to the house's cards and update the score
            while house_score != 0 and house_score < 17:
                house_cards.append(deal_card())
                house_score = calculate_score(house_cards)
            
            # Show the updated cards
            print(f'\nYour cards: {user_cards}, Your current score: {user_score}')
            print(f'\nHouse cards: {house_cards}, House current score: {house_score}')
            
            # Compare the scores and print the winner
            print(compare_scores(user_score, house_score))
            
            desicion = input("\nWould you like to play again? (y/n): ")

            # If the users wants to play again, clear the screen and restart the game
            if desicion == "y":
                game_ended = True
                # Clear the screen for better readability, clear only works on macOS and Linux (posix) while cls only works on Windows (nt)
                if(os.name == 'posix'):
                    os.system('clear')
                else:
                    os.system('cls')
                                
                blackjack()
            # If the user is done, exit the game
            else:
                print("\nThanks for playing!")
                game_ended = True

    blackjack()
    
if __name__ == "__main__":
    main()