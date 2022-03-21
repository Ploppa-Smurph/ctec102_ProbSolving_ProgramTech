# append a line to a file 'written.txt'
'''def write():
    file_name = input('enter a file name without extension: ')
    f=open(file_name+'.txt', 'w')
    newline=1
    while newline != '':
        newline = input('enter a new line of press enter to quit: ')
        f.write(newline+'\n')
    f.close()    
write()'''

def write():
    file_name = input('enter a file name without extension: ')
    f=open(file_name+'.txt', 'w')
    newline= input('enter the new line or press enter to quit: ')
    f.write(newline)
    while newline!='':
        newline = input('enter the new line or press enter to quit: ')
        f.write('\n'+newline)

    f.close()
write()
    
