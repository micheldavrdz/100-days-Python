import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]

print('Welcome to the Rock, Paper, Scissors game!')


move_selected = int(input('Please select your move (Type 0 for Rock, 1 for Paper or 2 for Scissors): '))


bot_selected = random.randint(0,2)

if move_selected < 0 or move_selected > 2:
    print('Please select a valid move!')
else: 
    print(f'\nYou selected: {hand[move_selected]}')

    print(f'The bot has selected: {hand[bot_selected]}')

    if((move_selected == 0 and bot_selected == 2) or (move_selected == 1 and bot_selected == 0) or (move_selected == 2 and bot_selected == 1)):
        print('You won!')
    elif((move_selected == 0 and bot_selected == 1) or (move_selected == 1 and bot_selected == 2) or (move_selected == 2 and bot_selected == 0)):
        print('You lost!')
    else:
        print('It\'s a draw!')
        