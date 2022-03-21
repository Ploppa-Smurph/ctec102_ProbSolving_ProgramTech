# program to read the data from 'numbers.txt' and add and provide sum
def sum():
    file_name=input('enter the data file to work from without extensions: ')
    infile=open(file_name+'.txt', 'r')
    total = 0
    for line in infile:
        line = line.rstrip('\n')
        total+=int(line)
        print(total)
        
    infile.close()
sum()
