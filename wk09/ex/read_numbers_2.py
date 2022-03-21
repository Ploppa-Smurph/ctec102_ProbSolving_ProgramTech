#open the file
myfile = open('random.txt', 'r')  # open function assigns the random.txt file into memory stored as the myfile variable

# Read the first line from the file
line = myfile.readline()   # read the first line of the file. Returns the information as a string.

#Continue processing the file
while line != '':    # we do not want to print the empty string resulting from using readline()
    print(line, end='')
    line = myfile.readline()   # this closes the loop at the end of the file
    
#close the file
myfile.close()
