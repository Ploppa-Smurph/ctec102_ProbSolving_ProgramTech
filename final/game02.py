import random

####################################################################
#  Constants
#####################################################################
border = print('\n', 50*'=', '\n', 50*'-', '\n', 50*'.')
NAME = ''
health = ''

####################################################################
#  Intro to the story
#####################################################################
print('\n', 'Welcome to the lands of Fluidity.', '\n', 'Where all is in constant motion', '\n', 'and the things you have learned have sometimes never happened.')

####################################################################
# User NAME
#####################################################################
NAME = input('By what NAME shall I address you? ')


###################################################################
# DICTIONARY for 'player' data
###################################################################    
player = {'name':NAME, 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':0}
border
print(NAME, 'You have begun your journey with', player['Health'], 'HEALTH')

####################################################################
# Create Dictionary for 'Realm' data
#####################################################################
def realm_set():
    realm = [
            'Egypt, the Year 4200BC',
            'Greece, the Year 3000BC',
            'India, the Year 1800BC',
            'Japan, the Year 0AD',
            'Korea, the Year 480AD',
            'France, the Year 1020AD',
            'Atlantic Ocean, the Year 1492AD',
            'North America, the Year 1888AD',
            'South America, the Year 2022AD',
            'Australia, the Year 2100AD'
    ]
    return realm


####################################################################
# Dictionary for 'movement' data - 10 Realms
#####################################################################
def move():
    dir = ''
    while dir != 'q':
        print('\n','You see portals that lie to the North "n", South "s", East "e", and West "w".')
        dir = input('Which portal do you choose? "n", "s", "e", or "w"? press "q" to quit.')
        if dir.lower() == 'n':
           pass
        elif dir.lower() == 's':
            pass
        elif dir.lower() == 'e':
            pass
        elif dir.lower() == 'w':
            pass
        elif dir.lower() == 'q':  # quit
            print('You have chosen to quit the game.')
        else:
            print('You have chosen an invalid direction, please choose "n", "s", "e", "w", or "q".')  # invalid direction



####################################################################
# Check for instance in realm 
####################################################################

####################################################################
# Dictionary for 'items' data - 5 items
#####################################################################
def item_dict():
    item = { 
            4200: 'Fire',
            0: 'Dagger',
            1888: 'Revolver',
            2022: 'Smartphone',
            2100: 'Unobtainium'
    }

####################################################################
# Dictionary for 'puzzles' data - 3 riddles
#####################################################################
def puzzle_dict():
    puzzle = {
        'What is Black, White, and read all over?': 'Newspaper',
        'What is more useful when broken?' : 'Egg',
        'I make 2 people of 1. What am I?' : 'Mirror'        
    }

####################################################################
# Maintain Health
#####################################################################
def health_gauge():
    pass
    
####################################################################
# Save
#####################################################################
def save():
    pass

####################################################################
# Load
#####################################################################
def load():
    pass

####################################################################
# main() function
#####################################################################
def main():
    pass

####################################################################
# call main()
#####################################################################
# main()
