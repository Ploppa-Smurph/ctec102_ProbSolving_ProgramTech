# FriendFace post
# user_id = 209
# message = "beans for sale"
# language = "en"
# date = "2020-01-01"
# location = (33.528, -112.26)    #as a tuple

# create dictionary of the object
post = {"user_id": 209, "message": "beans for sale", "language": "en", "date": "2020-01-01", "location": (33.528, -112.26)}

# create using a dictionary constructor
post2 = dict(message="finger foods?", language="en")  # notice we don't use "" around the key, and we use = (instead of :)
print(post2)

# dictionaries are Mutable -- we can add items to the dictionary 
post2["user_id"] = 117        # notice we use '' around the key again when adding with []
post2["date"] = "2020-01-02"

'''print('what happens when we try a key that is not there? ')
print(post2['location'])     # post 2 had no location'''

# checking for KeyError and creating exception
try:
    print(post2['location'])
except KeyError: 
    print('No location found')   

# see what methods the post2 dictionary has
dir(post2)   

# the .get method Returns a value for a key if it is in the dictionary, else it return <i>NONE</i> a default value
# we set the post2.get() method to a variable named 'loc'
loc = post2.get('location', None)
print(loc)

# .keys() method - loop through the keys in a dictionary
for key in post.keys():
    value = post[key]
    print(key, '=', value)

# you can also use the .items() method - this iterates through both keys and values 
for key, value in post.items():
    print(key, "=", value)
