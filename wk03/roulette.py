''' Roulette Wheel Colors
On a roulette wheel pockets are numbered from 0-36. Colors of the pockets are as follows:
0 = green
01 - 10 = odd = red; even = black
11 - 18 = odd = black; even = red
19 - 28 = odd = red; even = black
29 - 36 = odd = black; even = red 

write a program that asks user for pocket number. the program will output if the pocket is green, red, or black.
display an error message if the user enters a number outside the range of 0-36
'''
# only need to take an integer, not a float
pocket = int(input('Enter a number between 0 and 36 for the roulette wheel: '))
if pocket==0:
    print(pocket, " is green.")

#all other pocket cases
elif pocket >= 1 and pocket <= 10:
    if pocket%2==1:
        print(pocket, ' is red')
    else:
        print(pocket, ' is black')
elif pocket >= 11 and pocket <= 18:
    if pocket%2==1:
        print(pocket, ' is black')
    else:
        print(pocket, ' is red')
elif pocket >= 19 and pocket <= 28:
    if pocket%2==1:
        print(pocket, ' is red')
    else:
        print(pocket, ' is black')
elif pocket >= 29 and pocket <= 36:
    if pocket%2==1:
        print(pocket, ' is black')
    else:
        print(pocket, ' is red')
else:
    print('Input is not recognized. Please enter only whole numbers between 0 and 36.')                            