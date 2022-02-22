# This code is to be run on the Reeborg's World console.
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Maze instructions:

# Write a program using an if/elif/else statement so Reeborg can find the exit. 
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

# Code uses custom website functions to make the robot move like front_is_clear() and right_is_clear(), while also having to declare my own function to turn right.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# I use front_is_clear to make sure the robot first runs into a wall, since it can end up in an infinite loop (on very specific layouts) otherwise.
while front_is_clear():
    move()
    
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()