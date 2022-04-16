#create a CLASS

class Insect:
    # double underscore = Private Method
    def __init__(self,name):  # self is a class variable which references the object being created
        # the name is an attribute for the object - below we are storing the attribute in a variable named 'name'
        self.name=name
        
    def catch(self, insect_obj):
        if insect_obj.name == 'fly' and self.name == 'spider':
            print('Caught a fly! Yummy!')
        elif insect_obj.name == 'fly' and self.name == 'fly':
            print('playing with another fly! Fun Times!!')
                    
fly1=Insect('fly')
fly2=Insect('fly')
spider1=Insect('spider')

spider1.catch(fly1)

fly1.catch(fly2) # this is because of the public method (catch)