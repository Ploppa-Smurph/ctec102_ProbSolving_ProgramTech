####################################################################
#  Constants
#####################################################################
border = print('\n', 50*'=', '\n', 50*'-', '\n', 50*'.','\n')
NAME = ''

####################################################################
#  Intro to the story
#####################################################################
print('Welcome to the lands of Fluidity.', '\n', 'Where all is in constant motion and the things you have learned have sometimes never even happened.')

####################################################################
# User NAME
#####################################################################
NAME = input('By what NAME shall I address you? ')


###################################################################
# DICTIONARY for 'player' data
###################################################################
def player():    
    player = {'name':NAME, 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':0}
    border
    print(NAME, 'You have begun your journey with', player['Health'], 'HEALTH')


####################################################################
# Dictionary for 'movement' data - 10 Realms
#####################################################################
def move():
    dir = ''
    while dir != 'q':
        border
        print('You see portals that lie to the North "n", South "s", East "e", and West "w".')
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
# Create Dictionary for 'Realm' data
#####################################################################
def realm_dict():
    realm = {
            '4200BC': 'Egypt, the Year 4200BC',
             '3000BC': 'Greece, the Year 3000BC',
             '1800BC': 'India, the Year 1800BC',
             '0AD': 'Japan, the Year 0AD',
             '880AD': 'Korea, the Year 480AD',
             '1020AD': 'France, the Year 1020AD',
             '1492AD': 'Atlantic Ocean, the Year 1492AD',
             '1888AD': 'North America, the Year 1888AD',
             '2022AD': 'South America, the Year 2022AD',
             '2100AD': 'Australia, the Year 2100AD'
             }
    return realm

####################################################################
# Check for instance in next realm 
####################################################################

####################################################################
# Dictionary for 'items' data - 5 items
#####################################################################
def item_dict():
    item = {
        
    }

####################################################################
# Dictionary for 'puzzles' data - 3 riddles
#####################################################################
def puzzle_dict():
    puzzle = {
        
    }

####################################################################
# Maintain Health
#####################################################################
def health_gauge():
    pass

####################################################################
# Save
#####################################################################

####################################################################
# Load
#####################################################################

####################################################################
# main() function
#####################################################################
def main():
    pass

####################################################################
# call main()
#####################################################################
# main()