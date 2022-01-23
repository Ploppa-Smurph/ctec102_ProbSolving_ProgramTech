#get user input
number = input('enter a number: ')
#input is returned as str and needs to be converted to int -- but will fail if someone enters a float
#number = int(number)
#let's use the float so we can use ints or floats
number = float(number)
print('your number plus 5 is: ',number+5)

#this can be combined to:
number = float(input('please enter a number: '))
print('your number plus 3.5 is: ', number+3.5)
