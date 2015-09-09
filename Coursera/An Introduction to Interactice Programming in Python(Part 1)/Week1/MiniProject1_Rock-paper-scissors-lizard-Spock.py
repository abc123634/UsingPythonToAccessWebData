# Rock-paper-scissors-lizard-Spock template
#author: Lee Meng
#URL: http://www.codeskulptor.org/#user40_gcYgU2vecz_0.py
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """Transfer 5 choices of names into corresponding numbers from 0 to 4."""
    name = name.lower()
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        another_name = raw_input("Enter your choice from 5 specific choices:")
        return name_to_number(another_name)


def number_to_name(number):
    """Transfer 5 choices of numbers from 0 to 4 into corresponding names."""
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        another_number = raw_input('Please give a number ranges from 0 to 5(exclusive):')
        return number_to_name(another_number)

def rpsls(player_choice): 
    """Simply display user's choice and compare it with the randomized 'computer choice'
        to decide who win the games."""
    
    print
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0, 5)
    computer_choice = number_to_name(computer_number)
    print 'Computer chooses', computer_choice

    difference = (player_number - computer_number) % 5
    if difference == 0:
        print 'Player and computer tie!'
    elif difference == 1 or difference == 2:
        print 'Player wins!'
    else:
        print 'Computer wins!'

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

"""Thanks for your patience :D"""


