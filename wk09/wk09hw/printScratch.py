
file = open('fruits.txt', 'r')

fruit = file.readlines()

num=0    # set a num variable for the number of the item, starting with value 0
for line in fruit:
        line=line.rstrip('\n')
        print(num, line)
        num+=1  #iterate through the items adding +1 to the variable num

try:
    userInput = int(input("enter the line number you would like to see: "))
    print(fruit[userInput])
except IndexError as var_error:
    print('The number listed was not in range of the current list', var_error)
except ValueError as var_error:
    print('Line number should be listed as a numerical value', var_error)
except:
    print('An error has occured')

file.close()

