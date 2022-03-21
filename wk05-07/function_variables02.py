# global
x = 10

print ('before', x)

def f():
    x=1
    print('local variable x:', x)
f()
print('after', x)    