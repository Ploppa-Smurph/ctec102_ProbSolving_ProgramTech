# Socratica - Sets Video 'https://www.youtube.com/watch?v=sBvaPopWOmQ'

example = set()
print(dir(example)) # .add()
print(help(example.add))

# add to a set -- you can add different data types to a set
example.add(42)
example.add(False)
example.add(3.14)
example.add('Thorium')

print(example)

print(len(example))

example.remove(42)
print(example)
print(len(example))

print(help(example.discard))
