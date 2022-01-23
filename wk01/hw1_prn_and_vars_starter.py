
#Q1 (3 pts) uncomment the next line and run the program:
print('Hi all. I am your first homework')


#Q2 (3 pts) Uncomment the next line the next line of code and debug:
print("I'll be learning python this semester!")
#the result should be printed on console as:
#I'll be learning python this semester!

# Q3 (4pts) Modify the code below to ask the user to input the first and last name in for the variables below.
#Hint: use input()
first_name=input('Please enter your First name: ')
last_name=input('Please enter your Last name: ')

#(3pts) Change the separator to print the  first_name and last_name under each other
print(first_name, last_name, sep='\n')

# Q4  Vlad is buying a piece of ham in the store. The price and weight of the ham is  given below.
price_per_pound=1.99 # $ per pound
weight=2.35  # lb
# (3 pts) Compute the total cost of the ham
print(first_name + ' bought ' + str(weight) + ' lb(s) of ham at $1.99 per pound.')
ham= float(price_per_pound) * float(weight)
format_ham=format(ham,'.2f')
# (4 pts)  Print the resulting cost. Make sure to format your cost to 2 decimal points 
print('the total cost of the ham purchased is $' + str(format_ham))


