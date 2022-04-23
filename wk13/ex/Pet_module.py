# write a pet class with attributes: __name, __animal, __age
# Pet Class __init__ method; get_name & set_name, get_animal & set_animal, get_age & set_age

# Write Program that creates an object of the class that
# asks user for a pet name, animal type, and age

class Pet:

    def __init__(self, name, animal, age):
        self.__name = name
        self.__animal = animal
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_animal(self):
        return self.__animal
    def set_animal(self, animal):
        self.__animal = animal

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return 'This is ' + self.__name + ' it is a(n) ' + self.__animal + ' and is ' + str(self.__age) + ' years old.'
