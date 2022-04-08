'''
1.write a function to add items to the phonebook (dictionary).
-user will enter a name and phone number
-that data will be added to a dictionary as a new Key-Value pair
2.display the phonebook
3. write a function to search by name and display the phone #
4. lear to save/load the phonebook with 'pickle'
5. write the main for the application
'''
#import pickle
import pickle

# primed the Dictionary and added 1 entry
phonebook = {'vlad':'123-4567'}   

# function to add new entries
def new_phone():   
#ask for input
        newName = input('Enter a new name or: ')
        if newName in phonebook:
            print('That name is already in the phonebook.', newName, phonebook[newName])
#update phonebook dictionary
        else:
            newNum = input('Enter a new number: ')
            phonebook[newName] = newNum    

# search for name in phonebook and return a phone number        
def find_name():
        search = input('Please enter a name: ')
        print(search, phonebook.get(search, ',that name is not in the phonebook.'))
        
# typical way to print out Dictionary
def print_phonebook():
    for key, value in phonebook.items():
        print('Name: ', key, 'Phone #: ', value)


def main():
    select = ''
    while select !='q':
        select=input('Type "n" to add a new entry, "v" to view an existing entry, "p" to print the phonebook, or "q" to quit: ')
        if select == "q":
            print('Goodbye')
        elif select == "n":
            new_phone()    
        elif select == "v":
            find_name()
        elif select == "p":
            print_phonebook()
        else:
            print('incorrect choice')


main()        
