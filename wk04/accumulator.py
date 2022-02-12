# running total program

def addNums(startNum, endNum):
    total = 0
    for i in range(startNum, endNum + 1):  # increment 1 additional time
        # total = total + i         # running total accumulator (called an Accumulator)
        total += i   #a simpler programming way to type the above -- total = total + i
    print(total)

addNums(1, 3)    
