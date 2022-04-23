class Farmer:
    def __init__(self, name, mood):
        self.__name = name
        self.__mood = mood

# getters and setters for name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

# getters and setters for mood
    def get_mood(self):
        return self.__mood
    def set_mood(self, mood):
        self.__mood = mood


    def talk_to(self, another_farmer):
        int(self.get_mood())
        if self.get_mood() <= another_farmer.get_mood():
            self.__mood += 1
        else:
            self.__mood -= 1

    def __str__(self):
        return 'Farmer ' + self.get_name() + ' is feeling like a ' + str(self.get_mood()) + ' on a scale of 10'
