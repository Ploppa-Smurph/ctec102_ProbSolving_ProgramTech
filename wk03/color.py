# primary colors are defined as red, blue, yellow. you can mix primary colors with each other to create secondary colors
'''mix red and blue == purple
mix red and yellow == orange
mix blue and yellow == green

-Design a program that prompts a user to enter the names of 2 primary colors to mix. 
if any input other than "red", "blue", or "yellow" are entered than return an error statement.
if correct operands are entered than the program should display the name of the secondary color
'''
print('This Amazing Program will give you the name of the resulting Secondary color when you, the user provides 2 primary colors.')
print('Enter 2 different primary colors below, choose from: red, yellow, or blue.')
color1 = input('Enter your first primary color (lower case only): ')
color2 = input('Enter the second primary color (lower case only): ')

'''if color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
    print('The Secondary Color when you mixed those 2 primary colors is: Purple')
elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
    print('The Secondary Color when you mixed those 2 primary colors is: Orange')
elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
    print('The Secondary Color when you mixed those 2 primary colors is: Green')
else:
    print('There was an input error, please make certain to enter a different primary color for each prompt and to enter the color in all lowercase letters.')'''
    
# another way to do it is to have the smaller color variable value (via the ascii value, ex: 'blue' would come before 'red')
if color1>color2:
     color1,color2=color2,color1

if color1=='blue' and color2=='red':
    print('the result is purple')
elif color1=='red' and color2=='yellow':
    print('the result is orange')
elif color1=='blue' and color2=='yellow':
    print('the result is green')
else:
    print('the input was invalid, please try again. enter the primary color in all lowercase')
# this has the same result as my above code using the 'and' 'or' but is much less clunky
