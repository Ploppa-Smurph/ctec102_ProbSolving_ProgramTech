# get an input for the number of asterisks as a banner
# should this be a while or for problem??
# we can use a 'for-loop' in this instance since we know the number being inputted
print('This program asks the user to input a number of "Stars" <asterisks> they want to see printed across the page and prints them out from top left to right')
def dispBan(stars):
    for count in range(stars):
        print('*', end=' ')  # - formats the asterisks (stars) so that they go across the screen [as opposed to down the screen] 
    print() # - prints blank line at end of program
starNum = input('How many stars do you want to see in the sky?: ')
dispBan(int(starNum))