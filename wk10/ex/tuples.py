import sys  # imports the sys module to use the 'getsizeof' function

#list ex:
prime_num = [2, 3, 5, 7, 11, 13, 17]

#tuple ex:
prefect_sq = (1, 4, 9, 16, 25, 36, 49)

#display length
print('# of primes:', len(prime_num))
print('# of squares:', len(prefect_sq))

#iterate over sequences
for p in prime_num:
    print("prime:", p)
for n in prefect_sq:
    print("square:", n)
    
print('List Methods')
print(dir(prime_num))
print(80*'-')
print('Tuple Methods')
print(dir(prefect_sq))

print('List size: ', sys.getsizeof(prime_num))
print('Tuple size: ', sys.getsizeof(prefect_sq))