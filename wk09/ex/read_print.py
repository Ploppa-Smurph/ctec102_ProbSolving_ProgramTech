# read from a file

'''infile=open('fruit.txt', 'r')
x=infile.read()
print(x)
infile.close()'''

# here is a better version stripping the end of the line formatting
'''infile=open('fruit.txt', 'r')
for line in infile:   # uses iteration to go through the lines of the file
    line=line.rstrip('\n')  # .rstrip() removes the formatting 
    print(line)
infile.close()'''

# wrapping the code inside a function is a better way to write the program
'''def main():
    infile=open('fruit.txt', 'r')
    for line in infile:
        line = line.rstrip('\n')
        print(line)
    infile.close()
main()'''    

# the code that also adds a number to each item of the list (enumerating)
def read():
    infile=open('fruit.txt', 'r')
    num=1    # set a num variable for the number of the item, starting with value 1
    for line in infile:
        line=line.rstrip('\n')
        print(num, line)
        num+=1  #iterate through the items adding +1 to the variable num
    infile.close()
read()