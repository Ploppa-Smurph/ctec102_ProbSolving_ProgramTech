#from Bill Barry's video on File I/O
import random 

#open the file
myfile = open('random.txt', 'w')  # opens file for writing

# write 100 random numbers file
for count in range (100):      
    number = random.randint(1,100)
    myfile.write(str(number) + '\n')
    
# close the file and confirm
myfile.close()
print('Process Complete')