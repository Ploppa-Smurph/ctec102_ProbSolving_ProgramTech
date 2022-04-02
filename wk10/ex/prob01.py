'''Total Sales
Design a program that asks users to enter a store's sales for each day of the week.
The amounts should be stored in a list.
Use a loop to calculate the toal sales for the week and display the result'''

sales_today= float(input('enter daily sales, or -1 to quit: ')) # get input to prime the variable
sales = [] # create the empty list to hold sales_today values
while sales_today != -1:
    sales.append(sales_today)
    sales_today = float(input('enter daily sales, or -1 to quit: '))

total = 0   #primed the total variable        
for num in sales:
    total+=num
print('total: ', total)
