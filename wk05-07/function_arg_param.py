#product function - value retaining
#these variables in the parens 
A = 2
def f(value1, value2):
    return A*value1+value2

#variables - used as arguments 
x=5
y=3

#add result
result = f(x,y)  #will not have same result as f(y, x)

#call function
print(result)     
