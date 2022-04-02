list = [12,13,14]
print(list)
print(list*2)
L=[x**2 for x in range(1,10)]
print(L)
print(L[1:5])
print(L.reverse) #reverses the list and changes the list (reverses and saves changes)
L[::-1] 
print(L[::-1])
L[-2]= 18  #changed the 
print(L)
print(50 in L)  # check to see if a value is contained within the list, False for 50
print(49 in L)  # this returns True
L.append('Howdy') # adds value to the end of the list
print(L)
print(L.index(18))  # gives the index location of the value 18 (7 in this ex)
L.insert(2, 777) # will insert the value 777 at index 2
print(L)
print(L.index(18)) # now the index location is 8 
del L[-1]    # deletes the last index value from the list
L.sort()  #sorts the list for you
print(L)
M = [] + L  # to make a copy of the list you must create a blank list and + add the list information to the new variable
print(M)
