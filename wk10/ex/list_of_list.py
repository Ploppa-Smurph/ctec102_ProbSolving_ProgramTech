'''write a program that maintains a list of lists.
each list contains a first name, a last name, and age
the program should be able to append and return records
'''
people = [['jeff', 'walley', 46],['james','walley', 16],['ra', 'martin', 40]]

def add_person():
    first = input('please enter a first name: ')
    last = input('please enter a last name: ')
    age = input('please enter the age: ')
    new = [first, last, age] 
    people.append(new)    


def print_last_name():
   for i in range(len(people)):
       print(people[i][1])

def main():
    action = ''
    while action != 'quit':
        action = input('choose an action: add, print <last names>, or quit: ')
        if action == "add":
            add_person()
        elif action =='print': 
            print_last_name()
        elif action =='quit':
            print('Thank you and goodbye')
        else:
            print('not a valid choice')
main()            
