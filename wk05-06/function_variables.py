#global variable
x=10
x+=1

print(x)

def f():
    #z is a local variable
    z=x*2
    print(z)
f()