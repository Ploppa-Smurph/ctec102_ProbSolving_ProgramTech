# call in module
import random

# void function
'''def roll_dice():
    value = random.randint(1,6)
    print('you rolled', value)
    
roll_dice()'''

# roll 2 random dice
def roll_2():
    value = random.randint(1,6) + random.randint(1,6)
    print('you rolled', value)

roll_2()    
