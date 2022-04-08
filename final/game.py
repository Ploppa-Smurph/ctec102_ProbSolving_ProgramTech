print('Welcome to the lands of Fluidity. Where all is in constant motion and the things you have learned have sometimes never even happened.')
print(50*'-')
print(50*'=')
print(50*'-')
NAME = input('By what NAME shall I address you? ')




###################################################################
# DICTIONARY for 'player' data
###################################################################
player = {'name':NAME, 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':0}

print(player['name'])
print(NAME, ' You have your journey with', player['Health'], ' Health')
