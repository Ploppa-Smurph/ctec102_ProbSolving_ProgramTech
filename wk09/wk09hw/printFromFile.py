'''Print a Line from a File 

Read from text file fruits.txt - utility program will print line from file selected by user.
If user inputs a line number that is too large return an error message.
    1- initialize counter variable to count line and a variable to store the user input.
    2- read lines using a loop and update the counter on every iteration
    3- when counter variable equals the user number then print the line
    4- include try-except after confident that everything works
'''
######################################################################
# define the method
######################################################################
def read():

######################################################################
# open the file
######################################################################
    file = open('fruits.txt', 'r')

    line = file.readlines()

try:
    userInput = int(input("enter the line number you would like to see: "))
    print(fruit[userInput])
except IndexError as var_error:
    print('The number listed was not in range of the current list', var_error)
except ValueError as var_error:
    print('Line number should be listed as a numerical value', var_error)
except:
    print('An error has occured')
         

######################################################################
# close the file
######################################################################
    file.close()

######################################################################
# call the method
######################################################################
read()




