# input validation loop

def showMenu():  # creating a function with no parameters

 # display the menu
    print('Employee Records Menu')
    print('---------------------')
    print('1. Search for Employee')
    print('2. Add Employee')
    print('3. Delete Employee')
    print('0. Exit')
    print()

 # get the input -- we do not know how many times we will need to loop, and we don't know if there is any collection of data that we are processing 
    menuChoice = -99    # set an invalid choice to prime the loop
    while menuChoice < 0 or menuChoice >3:
        menuChoice = int(input('Select option: '))
    print('You chose:', menuChoice)
showMenu()
