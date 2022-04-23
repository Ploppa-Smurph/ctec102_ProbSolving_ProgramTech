# works with Pet_module.py
import Pet_module

name = input('What is your pet\'s name? ')
animal = input('What type of Animal is your pet? ')
age = int(input('What is ' + name + '\'s age? '))
a_pet = Pet_module.Pet(name, animal, age)
print(a_pet)

print('Your pet\'s name is '+ a_pet.get_name())
print('The pet is a ' + a_pet.get_animal())
print(a_pet.get_name() + ' is', a_pet.get_age(), 'years old.')
