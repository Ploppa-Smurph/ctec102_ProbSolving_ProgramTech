# create a dictionary 'd' uses {'curly':'braces', 'seperated':'by commas', 1:2}
d = {1:4, 'hello':'world'}
print(d)
print(d[1])
print(d['hello'])
print('is 5 in dictionary d? ')
print(5 in d)
# to add to the dictionary
d['added'] = 'this value'
print(d)
# lets remove / delete a key-value pair
del d[1]
print(d)
# example for our final project of using a dictionary to hold data
player = {'name':'Hero', 'Health':10, 'has sword':False, 'has key':False, 'solved puzzle':0}
print(player)
print(player['name'])
print('Health: ', player['Health'])
