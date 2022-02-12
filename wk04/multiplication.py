# create the function 
def multTab(maxNum):
    
# we need to display our output in rows and columns    
    # we will be using for-loops for the nested loop, the interior loop will have to finish running before the outer loop can increment again
    for row in range(1, maxNum + 1): # add the +1 to properly increment the loop, otherwise it will stop 1 short of what we our maxNum
        for col in range(1, maxNum + 1):
           #print(row * col, end=' ')     -- this will not format the table how we would like

            print(format(row * col, '5d'), end='')   # this will format the printout with '5d' space per character - that is a digit amount
        print()  # by printing this blank line when the columns are finished printing we are now able to start our new row
            
multTab(10)            
