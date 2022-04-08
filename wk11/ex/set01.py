# working with Sets
A = {1,2,3}
B = {4,5,6}
C = {5,6,7}
D = set()
len(A)
A.add(4)
print(A)
D = set([1,2,3,4,5,6,2,1,3,4,5])
print(D)

# check to see if an item is in a set
print ('is 10 in D')
print(10 in D)
print(D)
print('now we see why it was False')

#iterate through a set
for x in D:
    print(x)   

