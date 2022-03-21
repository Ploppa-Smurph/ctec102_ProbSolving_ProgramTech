# Append a line to a file
'''f=open('blah.txt', 'a')
f.write('abbra kadabra')
f.close()'''

# Append with a new line for easier reading
'''f=open('blah.txt', 'a')
f.write('parlor tricks\n')  #= creates a new line at end of the code
f.close()'''

# Append with user input
def append():
    f=open('blah.txt', 'a')
    newline='1'
    while newline !='':
        newline = input('enter the new line or press enter to quit: ')
        f.write(newline+'\n') # concatenate a new line on the end of the string
    f.close()
append()

# remove a file
import os # imports the os library into Python
def remove():
    os.remove('blah.txt')
remove()    