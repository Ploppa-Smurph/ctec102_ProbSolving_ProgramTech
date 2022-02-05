#check the grade input and give the resulting letter grade
# use if-elif-else statements to reduce the amount of indentation and make the code easier to write and human-read

print('I am the Grading Computer. Enter your numerical score value and your Letter Grade will be returned through Digital Magic')
grade=float(input('What was your score? '))

if grade >= 90:
    print('Your grade is: A')
elif grade >= 80:    
    print('Your grade is: B')
elif grade >= 70:    
    print('Your grade is: C')
elif grade >= 60:    
    print('Your grade is: D')
else:    
    print('Your grade is: F')
 