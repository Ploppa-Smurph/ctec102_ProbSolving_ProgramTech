myset = set()
print(myset)

#add items to the set 1 at a time
myset.add('alpha')
myset.add(2)
myset.add(3.14)
myset.add(('a', 'b', 'c'))
print(myset)


# add a list to a set
myset = set('abcdefghijklmnopqrstuvwxyz')
print(myset)
print('it breaks the letters down into individual characters and stores them unordered. When you print them out you get alphabet soup!')

# in order to pass a list of strings you have you put the list in brackets
myset = set(['john', 'paul', 'george', 'ringo'])
print(myset)

# using the .add() method
myset.add('Eric') # add Eric to the set without using brackets
print(myset)

# .remove() method
myset.remove('Eric') # remove Eric from the set -- Will throw an Exception if the item does not exist 
print(myset)

# .discard() method
myset.discard('Phillip') # discards Phillip from the set if it is there -- Will NOT throw an Exception if the item was not there

'''
There are additional methods that you can use on sets --  
        .update() - which allows you to update items in a set, merge sets, and merge lists and sets
        .cleare() - clears ALL the items in a set               
        '''
# for loop to iterate over items in a set
# using 'in' and 'not in' operators

'''UNION, INTERSECTION, DIFFERENCE, SYMMETRIC DIFFERENCE, SUBSET, and SUPERSET'''

#Union
print('do you know what the Union of 2 sets is? it is a set that contains ALL of the elements of BOTH sets.')
set02 = set(['paul', 'lance', 'hank', 'johnny'])
print('this is myset:', myset)
print('this is set02:', set02)
set3 = myset.union(set02)
print('this is the union of myset and set02:', set3)

# Intersection
print('have you heard of an intersection? it is a set that contains ')
intersection = myset.intersection(set02)
print('this is the intersection of myset and set02: ',intersection)
intersection02 = set02.intersection(myset)
print('this is the intersection of set02 and myset: ',intersection02)

#Difference
print('what is the difference between 2 sets, you can use the "-" operator? a set that contains the elements that are Different from the 1st set to the second set.')
difference = myset.difference(set02)
print('this is the difference of myset - set02: ',difference)
difference02 = set02.difference(myset)
print('this is the difference of set02 - myset: ',difference02)
print('the order makes a difference this time')

#SYMMETRIC DIFFERENCE
print('now i know you are wondering about symmetric difference, you can use the "^" operator, it is a set that contains the elements from both sets that are NOT in both sets already.')
sym = myset.symmetric_difference(set02)
print('this the symmetric difference of myset ^ set02: ', sym)

# kept getting Attribute errors with Subset and Superset
'''#SUBSET and SUPERSET
print('to find the Subset of 2 sets, you can use the "<=" operator. a subset is ')
set03 = ('123456')
set04 = ('1234')
print('working with 2 different sets now, set03 and set04', set03, set04)
print('we can see that set04 is a subset of set03: ', set04.<=(set03))
print('and that set03 is the superset of set04: ', set03.>=(set04))'''


