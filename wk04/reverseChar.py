# reverse characters in a string
# since a string is a 'collection' then we will use a 'for-loop' again

def strReverse(aString):
    revString = ''
    for ch in aString:
        revString = revString + ch
    print(revString)

strReverse('Hello')    
