print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island.')

print('\nYour mission is to find the treasure.')

print('\nStart the adventure!')

right_or_left = input('\nYou wake up one day in the middle of a road and see nothing in sight. You walk for a few minutes and the road splits in two, do you walk left or right? (right or left): ').lower()

if right_or_left == 'left':
    
    swim_or_wait = input('\nYou walk left and see a small river. Do you swim across or wait and see what happens? (swim or wait): ').lower()
    
    if (swim_or_wait == 'wait'):
        red_blue_or_yellow = input('\nSuddenly the atmosphere fills with smoke and 3 doors appear out of nowhere, do you enter the red, blue or yellow one? (red, blue or yellow): ').lower()
        
        if (red_blue_or_yellow == 'red'):
            print('\nYou enter the red door and the whole room is a giant hole. The door closes behind you and you fall to your death. GAME OVER')
        elif (red_blue_or_yellow == 'blue'):
            print('\nYou enter the blue door and the it connects directly to space. The door closes behind you and you start floating in space. With no air you die of suffocation. GAME OVER')
        else: 
            print('\nYou enter the yellow door the whole place is covered in sand. As you keep walking you find a treasure chest. You open the chest and find gold. YOU WIN!')
            
    else:
        print("\nYou swim across the river and your right foot gets stuck in the water. As you try to release your foot, a bank of piranhas start to attack you. You don't have enough strenght to fight them off, so you get eaten. GAME OVER")
        
else:
    print('\nYou walk to the right and find nothing, on the way back a snake approaches and bites you in the leg, with no help nearby the venom acts too fast and you die alone. GAME OVER')