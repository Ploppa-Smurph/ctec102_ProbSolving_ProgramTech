direction = ''
####################################################################
#  Constants
####################################################################
border = print('\n', 50*'=', '\n', 50*'-', '\n', 50*'.','\n')
NAME = ''

####################################################################
#  Intro to the story
####################################################################
print('Welcome to the lands of Fluidity.', '\n', 'Where all is in constant motion and the things you have learned have sometimes never even happened.')

####################################################################
# User NAME
####################################################################
NAME = input('By what NAME shall I address you? ')


###################################################################
# DICTIONARY for 'player' data
###################################################################
def player():    
    player = {'name':NAME, 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':0}
    print(border)
    print(NAME, 'You have begun your journey with', player['Health'], 'HEALTH')

######################################################################
#
######################################################################
while direction != 'q':
    print()
    print('\n', 'You see portals that lie to the North "n", South "s", East "e", and West "w".')
    direction = input('Which portal do you choose? "n", "s", "e", or "w"? press "q" to quit.')
    
    if direction.lower() == 'n':
        if direction: 
            pass
        else: pass
        

    elif direction.lower() == 's':
        if direction: pass
        else: pass
        
    elif direction.lower() == 'e':
        pass
    
    elif direction.lower() == 'w':
        pass
    
    elif direction.lower() == 'q':  # quit
        print('You have chosen to quit the game.')
    
    else:
        print(
            'You have chosen an invalid direction, please choose "n", "s", "e", "w", or "q".')  # invalid direction
            
            