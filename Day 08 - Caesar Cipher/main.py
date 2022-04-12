def main():

    from logo import caesar_logo
    import os

    # We make an alphabet list for checking the user's input, doubled so the user can use words with all letters
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def caesar_cipher(user_text, shift_amount, cipher_direction):
        
        final_text = ''

        # We check the user's input letter by letter
        for letter in user_text:
            
            # Check if the input is actually a letter or not
            if letter in alphabet:
                
                # Now we get the index of the letter in the alphabet list
                letter_position = alphabet.index(letter)
                
                # if the user wants to encrypt the text we add the shift amount to the index (so a+2 becomes c, for example), if not we subtract the shift amount from the index (so c-2 becomes a, for example)
                if cipher_direction == 'encode':
                    new_letter_position = (letter_position + shift_amount)
                elif cipher_direction == 'decode':
                    new_letter_position = (letter_position - shift_amount)
                    
                final_text += alphabet[new_letter_position]
            
            # If the input wasn't a letter, we don't change it
            else:
                final_text += letter
                    
        print(f'\nYour {direction}d text is: {final_text}')
        
    print(caesar_logo)

    end_caesar = False

    # Keep the program running until the user decides to stop
    while not end_caesar:
        
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("\nType your message: ").lower()
        shift = int(input("\nType the shift number: "))
        
        # Make sure the shift number is between 1 and 26 (letters in the alphabet)
        shift = shift % 26

        # Call the caesar_cipher function with the user's input parameters
        caesar_cipher(user_text=text,shift_amount=shift, cipher_direction=direction)
        
        start_again = input("\nWould you like to encrypt or decrypt another message? (y/n): ")
        
        # if the user wants to start again, we clear the screen and start the loop again, if not we end the program
        if start_again == 'n':
            end_caesar = True
            print('\nSee you later!')
        else:
            # Clear the screen for better readability, clear only works on macOS and Linux (posix) while cls only works on Windows (nt)
            if(os.name == 'posix'):
                os.system('clear')
            else:
                os.system('cls')
            
if __name__ == '__main__':
    main()