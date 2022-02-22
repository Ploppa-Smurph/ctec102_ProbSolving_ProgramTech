# demo of what happens when you change the value of a parameters
def main():
    value = 99
    print('The value is', value)
    change_me(value)
    print('In main the value is', value)
    
def change_me(arg):
    print('I am changing the value. Old value was', arg)
    arg = 0
    print('Now the value is', arg)    