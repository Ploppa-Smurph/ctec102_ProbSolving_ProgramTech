# working with sets some more

A={1,2,3}
B={2,3,4}
print('what is the union() of A and B?')
print('A.union(B)')
print(A.union(B))
print('then why does A still equal')
print('A =', A)
print('did you know that the | pipe character will do the same thing?')
print('A|B is the same as A.union(B)')
print('A|B =', A|B)
print('you can use the difference() or - to find out which items are not contained in both sets')
print('A-B =', A-B)
print('B-A =', B-A)
print('Symetric Difference ^ will tell you which objects are in either set, but not in both')
print('A^B =', A^B)
print('Intersection = A.intersection(B)', A.intersection(B))
print('A&B is a shortcut for intersection, A&B =', A&B)
print('we can also determine SubSets <every element of A will be an element of B>')
print('A<=B', A<=B)
print('the above is False because every element of A is not contained in B')
print('{3}<=A ', {3}<=A, ' this is True because 3 is contained in A')
