#opens the random.txt file we just created with write_rand.py
myfile = open('random.txt', 'r')

# read each line in the file and display it using 'for' loop
for line in myfile:
    print(line, end='')   # or rstrip()
    
# close the file
myfile.close()