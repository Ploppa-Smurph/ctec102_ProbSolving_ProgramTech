'''
-Write a program that creates a list of friend names so that these who are Tigers fans are in the beginning of the list. 
    The friends who are not should be in the end of the list. The program should run for as long as the user wants to add names. 

-After the user adds a new name the program should ask if this friend is a Tigers fan. 
    If the the friend is a tigers fan, add the name to the beginning of the list, if not- to the end of the list.  

-When the user is done adding new names, print the list.
'''
######################################################################
#  Initialize
##################################################################### 
list = []
userInput = -99

######################################################################
#  Keep them in the loop
##################################################################### 
while userInput != 'quit':
    
    
    
######################################################################
#   Get the name
#####################################################################     
    userInput = input('Enter a name or "quit" to exit: ')
    if userInput != 'quit':

######################################################################
#  Tiger Fan?
##################################################################### 

        tigerFan = input('Is this person a Tiger fan? (y/n): ')
        if tigerFan == 'y':
            list.insert(0, userInput)
        else:
            list.append(userInput)
    else:
        print('Friend list, Tiger fans first: ', list)