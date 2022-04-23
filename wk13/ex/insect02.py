class Insect:
    def __init__(self, name):  # __var__ =  double underscore on both sides = 'standard' method
        self.__name = name  # __ = double underscore before = private or hidden

    # to make the code private you use Getters and Setters <like Java>
    def get_name(self):  # getter
        return self.__name  # return private attribute

    def set_name(self, new_name):  # setter
        self.__name = new_name  # set private attribute

    # public method which takes another obj as an argument
    def catch(self, other_insect_object):
        if other_insect_object.get_name() == 'fly' and self.__name == 'fly':
            print('Oh what fun, we can play!')
        else:
            print('A Spider is going to get me!')
        # create object instances based on the class

    def __str__(self):

        return 'this is an Insect object (instance): ' + self.__name

fly1 = Insect("fly")  # fly1 is an instance of an object, based on the Insect class
fly2 = Insect("fly")
spider1 = Insect("spider")  # spider1 is another instance of the object this one created as a 'spider' instance

# catch
spider1.catch(fly1)
print(spider1)
fly2.catch(fly1)
print(fly2)
fly1.catch(spider1)
print(fly1)
