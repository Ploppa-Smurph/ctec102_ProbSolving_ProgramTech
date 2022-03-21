# divide 2 numbers (m, n) provided by user
'''try:
    m= float(input('Enter a dividend: '))
    n= float(input('Enter the divisor: '))

    print('the Quotient of ', m,'divided by ', n, 'is ', m/n)

except:
    print('input error, please try again')'''


try:
    m= float(input('Enter a dividend: '))
    n= float(input('Enter the divisor: '))

    print('the Quotient of ', m,'divided by ', n, 'is ', m/n)

except ZeroDivisionError as err:
    print('Cannot divide by 0;', err)

except ValueError as err:
    print('Input must be in numeric format;', err)
