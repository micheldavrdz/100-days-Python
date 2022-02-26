def main():

    import os
    import operator
    from auction_logo import logo

    auction = []
    end_auction = False

    # Make a function to add new bidders to the auction (their name and bid amount)
    def blind_bidding(bidder, bid_amount):
        new_bidding = {}
        new_bidding['name'] = bidder
        new_bidding['amount'] = bid_amount
        
        auction.append(new_bidding)

    print(logo)

    print('\nWelcome to the blind auction program!')

    # Keep the program running until the user decides to stop (no more bidders)
    while not end_auction:
        name = input('\nWhat is your name?: ')
        bid = float(input('\nHow much do you want to bid?: $'))
        
        # Call the blind_bidding function with the user's name and bid amount
        blind_bidding(name, bid)
        
        decision = input('\nAre there any other bidders? (y/n): ')
        
        # If the user doesn't want to add any more bidders, we end the auction, else we clear the screen (so the next bidder can't see the last bid) and start the loop again
        if decision == 'n':
            end_auction = True
        else:
            # Clear the screen for better readability, clear only works on macOS and Linux (posix) while cls only works on Windows (nt)
            if(os.name == 'posix'):
                os.system('clear')
            else:
                os.system('cls')
    
    # Sort the auction list by the bid amount (highest to lowest)
    auction.sort(key=operator.itemgetter('amount'), reverse=True)

    # The first element in the auction list is now the highest bidder, so they win the auction
    print(f'\nThe winner is {auction[0]["name"]} with a bid of ${auction[0]["amount"]}!')

if __name__ == '__main__':
    main()

