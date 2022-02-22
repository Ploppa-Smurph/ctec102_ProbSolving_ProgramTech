import random
# will choose between array objects in list (this ex: True and False)
#random.choice([True, False])

# will give a random # between 1 & 10 (including 1 & 10)
#random.randint(1,10)

# small program to choose a random friend and a random message from a list and send a message to a friend, randomly!
def main():
    #value-returning function choose() assigns the value to the variables friend, message
    friend, message = choose()
    #void function that takes 2 arguments
    message_printer(friend, message)

def choose():
    fr=random.choice(['Ute','Elmo', 'Lanscky'])
    msg=random.choice(['We need to hangout', 'I miss you dearly', 'Do you have my money?', 'How about you cook me some dinner?'])
    return fr, msg
def message_printer(friend, message):
    print('Hello', friend+',', message)