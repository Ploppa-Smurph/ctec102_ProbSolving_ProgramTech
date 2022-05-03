import random


####################################################################
#  Constants
####################################################################
border = print('\n', 50*'=', '\n', 50*'-', '\n', 50*'.','\n')
direction = ''
puzTimer = random.randint(9,15)
itemTimer = random.randint(4,10)
encounter = random.randint(15,24)
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
    player = {'name':NAME, 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':True}
    print(border)
    print('\n' + NAME, 'You have begun your journey with', player['Health'], 'HEALTH')
    return player

#########################################################################
# SET for Realm 
#########################################################################
realm_Set = {'Ethiopia', 'Constantanoble', 'Unified Sphere HQ','Dansk','Swansea','Japan', 'Rome', 'Buenos Aires'}

############################################################################
# DICTIONARY for Puzzles
############################################################################
puzzle = {'What is black, white and read all over? ': 'a Newspaper'}

############################################################################
# List for Items
############################################################################
item = ['sword', 'key']

############################################################################
# Creature Class
############################################################################
class Creature: 
    def __init__(self, name, health, weapon):
        self.name = name
        self.__health = health
        self.__weapon = weapon

    def get_health(self):
        return self.__health
    def set_health(self, health):
        self.__health = health
        
    def get_weapon(self):
        return self.__weapon
    def set_weapon(self, weapon):
        self.__weapon = weapon
        
    def attack(self):
        attack_roll = random.randint(1,10)
        if attack_roll <= 2:
            print(self.name, 'attacks', player.name, 'with', self.__weapon)
            player.set_health(player.get_health() - 1)
            print(player.name, 'has', player.get_health(), 'health left')
        else:
            print(self.name, 'misses the attack')        
        
############################################################################
#
############################################################################

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
    print('\n', 'You see portals that lie to the North, South, East, and West.')
    direction = input('\nWhich portal do you choose? "n", "s", "e", or "w"? "q" to Quit and "i" for Information:  ')
    if direction.lower() == 'n':
        move()
        turn += 1
        print('Turn #: ', turn)
    elif direction.lower() == 's':
        move()
        turn += 1
        print('Turn #: ', turn)
    elif direction.lower() == 'e':
        move()
        turn += 1
        print('Turn #: ', turn)
    elif direction.lower() == 'w':
        move()
        turn += 1
        print('Turn #: ', turn)
    elif direction.lower() == 'q':  # quit
        print('\nYou have chosen to quit the game.')
    elif direction.lower() == 'i':
        print(player)
    else:
        print('\nYou have chosen an invalid direction, please choose "n", "s", "e", "w", "q", or "i".')  # invalid direction        
    
        
#######################################################################################################################
# Encounters
#######################################################################################################################        
    if turn == puzTimer:
        print('\nThere is something interesting in the  distance')
        puzzAnswer = input('\nA jester appears and blocks your way. He smiles and looks you in the eyes and states. I have a puzzle for you, ' + puzzle[0]) 
        if puzzAnswer.lower == puzzle[1]:
            puzzle['solved puzzle'] = True
            print('\nYou have solved the puzzle and have gained a puzzle point')
        puzTimer = -99
        
    elif turn == itemTimer:
        itemPop = item.pop()
        print('\nThere is something of use in the distance')
        print('\nA bauble catches your eye, it is a ' + itemPop)
        player['has ' + itemPop] = True
        print('\nYou have gained an item')
        itemTimer = random.randint(itemTimer + 2, itemTimer + 8)
    else:
        move() 
    '''elif turn == encounter:
        encounterPop = 
        print('\nThere is something ugly in the distance')
        encounter = random.randint(25, 34)'''
          
