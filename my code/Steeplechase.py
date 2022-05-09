"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    up()
    cross()
    down()
def down():
    while front_is_clear():
        move()
    turn_left()

def cross():
    turn_right()
    move()
    turn_right()
def up():
    turn_left()
    # Karel is facing north
    while not right_is_clear():
        move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def down():
    while front_is_clear():
        move()
    turn_left()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
