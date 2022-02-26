'''We say that BAZINGA of x and y is the value x*y+x+y. 
    For example if x=3 and y=5 the BAZINGA of 3 and 5 is 23 (we compute 3*5+3+5).

Write a program that asks a user to compute a BAZINGA of 2 randomly generated numbers. 
-The program should display the values x and y and ask the user to input the answer. 
-The user answer is then checked against the true answer. 
-If the user answer is correct, print an appropriate message. 
-If the user answer is wrong, print the correct answer. 
-You may only use concepts from Chapters 2 through 5 of the book to complete this assignment.

Notes and Hints:
The random numbers you generate should be between 0 and 10
It is convenient to write a function bazinga(x,y) to return the true answer. 
Then use this answer in the main() to compare against the user answer. ''' 


#######################################################################################################
#       Import
#######################################################################################################
import random


#######################################################################################################
#       Constants
#######################################################################################################
X= random.randint(0,10)
Y= random.randint(0,10)

#######################################################################################################
#       Main
#######################################################################################################
def main():
    bazingaCalc = bazinga(X,Y)
    

    if userAns == bazingaCalc:
        print('Your brain power is admirable, you entered the correct answer')  
    else:
        print('Perhaps you would like to recheck your math. The Correct answer is: ', bazingaCalc)
        


#######################################################################################################
#       Calculate 
#######################################################################################################    
def bazinga(X,Y):    
    bazingaNum = X*Y+X+Y
    return bazingaNum    
    
#######################################################################################################
#       Output
#######################################################################################################
print('Welcome to the Amazing Game of BAZINGA!!!')
print('-----------------------------------------', end='\n')
print('You will be given 2 random numbers between 0 & 10.')
print('In order to solve the puzzle you must use the formula: x*y+x+y')      
print('The Numbers you have been dealt are:')
print('-*-'*10)
print(' x - ', X,' and y - ', Y, end='\n')

#######################################################################################################
#       Input
#######################################################################################################
userAns = int(input('What is your answer? '))    
    


#######################################################################################################
#       Call main Function to Run
########################################################################################################  
    
main()    
