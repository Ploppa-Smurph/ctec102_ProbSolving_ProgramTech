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
NAME = input('\nBy what NAME shall I address you? ')


###################################################################
# DICTIONARY for 'player' data
###################################################################
def player():    
    player = {'name':NAME, 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':0}
    print(border)
    print('\n' + NAME, 'You have begun your journey with', player['Health'], 'HEALTH')

#########################################################################
# SET for Realm 
#########################################################################
realm_Set = {'Japan', 'Rome', 'Pacific', 'Portland', 'New Buenos Aires'}

###########################################################################
#  Move Function
############################################################################
def move():
    realm = realm_Set
    if len(realm) <= 1: 
            realm = {'Japan', 'Rome', 'Pacific', 'Portland', 'New Buenos Aires'}
            realm = realm.pop()
            print('\nYou have arrived in ' + realm)
    else: 
            realm = realm_Set.pop()
            print('\nYou have arrived in ' + realm)


######################################################################
# Navigation 
######################################################################
turn = 0
while direction != 'q':
    print()
    print('\n', 'You see portals that lie to the North, South, East, and West. Beyond each portal there flicker scenes of various lands and times, random and exotic.')
    direction = input('\nWhich portal do you enter? "n", "s", "e", or "w"? "q" to Quit and "i" for Inventory:  ')
    
    
    if direction.lower() == 'n':
        move()
        turn += 1
        player()
        print('Turn #: ', turn)    
    elif direction.lower() == 's':
        move()
        turn += 1
        player()
        print('Turn #: ', turn)
    elif direction.lower() == 'e':
        move()
        turn += 1
        player()
        print('Turn #: ', turn)  
    elif direction.lower() == 'w':
        move()
        turn += 1
        player()
        print('Turn #: ', turn)
    elif direction.lower() == 'q':  # quit
        print('\nYou have chosen to quit the game.')
    elif direction.lower() == 'i':
        player()
    else:
        print('\nYou have chosen an invalid direction, please choose "n", "s", "e", "w", "q", or "i".')  # invalid direction
        
        
            
            
