# working with loops and the Fibonacci sequence
def fibonacci (limit):
    print('This program outputs the Fibonacci sequence to a preset end limit, the current limit is', limit)
  #setup the initial numbers to start the count  
    num1 = 1
    num2 = 1
    # formatting the print so that it reads better
    # print(num1, num2,end=', ')
    print(num1, end=', ')
    
    # setting up the condition. we will iterate through the data until num2 has reached the defined limit of fibonacci
    while num2 <= limit:
    # creating newNum which will be the result of adding num1 and num2, we then set the num1 var == num2, set num2 == newNum so that we are ready to start the process again   
        print(num2, end=", ")
        newNum = num1 + num2
        num1 = num2
        num2 = newNum
    # print(num2, end=', ')  -- if the print is this late in the loop then there are problems when dealing with the next value; you go 1 over what is intended
         
        
        
        
        
fibonacci(5000)
