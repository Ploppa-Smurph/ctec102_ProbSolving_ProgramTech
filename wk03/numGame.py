'''
Game of Numbers -- ask user for to input an integer
1. if the number is divisible by both 9 and 5 print integer + "is a favorite number!"
2. if divisible by 9 (but not 5) then divide the number by 9 and print the result.
3. if divisible by 6 (but not 9) then print the original number with "is a cool number, too!"
4. if divisible by 3 (but not 9 or 6) then divide by 3 and print the result.
5. if the number is not divisible by 3 then print "not divisible by 3".
'''
print('Welcome to the Game of Numbers')
number=int(input('Please enter a whole number: '))
if number%9 == 0 and number%5 == 0:
    print(number, 'is a favorite number!')
elif number%9 == 0:
    print('the result is', number//9)
elif number%6 == 0:
    print(number, 'is a cool number, too!')
elif number%3 == 0:
    print('the result is', number//3)
else:
    print('not divisible by 3')            
