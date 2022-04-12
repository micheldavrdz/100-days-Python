# Import random for choice, os for clearing the screen
import random
import os
# Import hang_art and dictionary modules for words and images
from hang_art import hang_stages, logo
from dictionary import word_list

def main():
  display = []
  game_word = random.choice(word_list)
  word_length = len(game_word)
  lives = 6
  end_game = False

  # We fill the display list with underscores
  for letter in range(word_length):
      display.append('_')

  print(logo)

  # If the game is still going on
  while not end_game:
      
      # Ask user for a letter
      guessed_letter = input("\nGuess a letter: ").lower()
      
      # Clear the screen for better readability, clear only works on macOS and Linux (posix) while cls only works on Windows (nt)
      if(os.name == 'posix'):
        os.system('clear')
      else:
        os.system('cls')
      
      # If the letter is in display, we print a message telling the user they've already guessed that
      if guessed_letter in display:
        print(f'\nHey! You already guessed "{guessed_letter}"')
      
      # We check game_word, if the letter is in the position we're looking at, we replace the underscore with it
      for position in range(word_length):
          
          letter = game_word[position]
              
          if guessed_letter == letter:
                  display[position] = letter
      
      # If the letter isn't in the word, we tell the user and they lose a life            
      if guessed_letter not in game_word:
          print(f'\nOuch, "{guessed_letter}" is NOT in the word')
          lives -= 1
      
      # We print the current state of the game (How the word is looking like, and how our buddy is doing)
      print(f"\n{' '.join(display)}")
      print(hang_stages[lives])
      
      # If there're no more underscores in display, all letters have been guessed and we declare the game as won
      if '_' not in display:
          print('Wow, You Win!')
          end_game = True
      # If the user has no more lives, our buddy was hanged and we declare the game as lost
      elif lives == 0:
          print(f'Oh no, You Lose! The word was: {game_word}')
          end_game = True

if __name__ == '__main__':
  main()