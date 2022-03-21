# open the file
myfile = open('numbers.txt', 'r')

# read and display file contents
for line in myfile:  # for loop will iterate for every line in the file
    number = int(line)  # converts to integer for dealing with in the future
    print(number)
    
# close the file
myfile.close()    