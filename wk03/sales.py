#program takes an inputted 'sales' amount and determines if someone is awarded a bonus.
#to reach the bonus you must have sales > (greater than)
#we convert the string amount (from input) to a float, since we are dealing with a numerical amount

#sales = float(input('Enter the sales amount: '))
#if sales>50000:
#    bonus=500
#    print('You qualify for the bonus of $', bonus)
#else:
#    print('Keep trying to qualify for the bonus')

# a better way to code the same thing is by defining the variables at the beginning

bonus_treshold = 50000
bonus = 500
sales = float(input('Enter the sales amount: '))
if sales > bonus_treshold:
    print('your bonus is $', bonus)
else: 
    print('Keep trying to qualify for the bonus')