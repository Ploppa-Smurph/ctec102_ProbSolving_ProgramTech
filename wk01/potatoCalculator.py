#potates cost .99$ / lb - get user input for how many lbs of potatoes they want
#display the resulting cost, without tax, to output
print('Potatoes cost $0.99 per pound')
weight = float(input('what is the total weight, in pounds, of potates you will purchase?'))
#saving to variable 'total'
#avoid using constants in your code - create a variable for the constant so you can reuse it more easily.
per_pound = .99
tax=1.09
subtotal = weight*per_pound
total = subtotal*tax
formatted_total = format(total,'.2f')
print('you purchased ' + str(weight) + ' lb(s) of potatoes.')
print('your subtotal is $' + str(subtotal))
print('your total is $' + str(formatted_total))
