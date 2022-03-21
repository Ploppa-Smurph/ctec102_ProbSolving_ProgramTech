# calculates dog years given human years
# parameter: human age in years
# return: dog age in years

def main():
    '''validUserAge = False   # create a sentinel for the loop
    while not validUserAge:   # create a loop to make the program run again if there is an error'''
    userAge = -99
    while userAge < 0 or userAge > 120:  # loops program if userAge is less than 0 or more than 120
        try: 
            userAge = int(input('Enter your age (range 0-120 years): '))
        except ValueError:       #the keyword for that error is ValueError 
            print('Please enter age in integers.')
        '''else: 
            validUserAge = True  '''
    print ('That is', dogYears(userAge), 'in dog years.')

def dogYears(humanYears):
    return humanYears * 7

main()
