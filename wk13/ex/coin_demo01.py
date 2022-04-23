import random

# Coin class will represent a coin that can be flipped

class Coin:

    # __init__ method initializes 'sideup' data to 'Heads'

    def __init__(self):
        self.sideup = 'Heads'

    # 'toss' method generates a random number between 0 and 1
    # if '0' then sideup = 'Heads'
    # else sideup = 'Tails'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # 'get_sideup' method returns value referenced by sideup

    def get_sideup(self):
        return self.sideup

# 'main' function
def main():
    # Create object of Coin class
    my_coin = Coin()

    # display the side of the coin that is facing upwards
    print(my_coin.get_sideup(), 'is the winner of the flip')
main()
