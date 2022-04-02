list = [['jeff', 'walley'],['frank', 'herbert'],['dante', 'valentine']]
print(list)
# iterate through the list
for x in list:
    print(x)

#alternate way to iterate through indexes in the list using 'len' (length)
for i in range(len(list)):
    print(i, list[i])

# list of list ex: 2 (3x3 matrix)
L = [[1,2,3],[4,5,6],[7,8,9]]  # think of this as 3 rows of information, row 1 = 1,2,3; row 2 = 4,5,6; row 3 = 7,8,9

#print the last element in each list
for i in range(len(L)):
    #print(L[i][2])  #this will print the last element
    print(L[i][-1])   # this will also print the last element from each list in the list
