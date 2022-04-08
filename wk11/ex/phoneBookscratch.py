'''
1.write a function to add items to the phonebook (dictionary).
-user will enter a name and phone number
-that data will be added to a dictionary as a new Key-Value pair
2.display the phonebook
3. write a function to search by name and display the phone #
4. lear to save/load the phonebook with 'pickle'
5. write the main for the application
'''
# primed the Dictionary and added 1 entry
phonebook = {'vlad':'123-4567'}

# function to add new entries
def new_phone():   
#ask for input
    newName = input('Enter a new name: ')
    if newName in phonebook:
        print('That name is already in the phonebook.', newName, phonebook[newName])
        
#update phonebook dictionary
    else:
        newNum = input('Enter a new number: ')
        phonebook[newName] = newNum    
        select()
        
# search for name in phonebook and return a phone number        
def find_name():
    search = input('Please enter a name: ')
    print(search, phonebook.get(search, ',that name is not in the phonebook.'))
    select()
    
def print_phonebook():
    print(phonebook)
    select()
    
def select():
    print('Welcome to the phonebook, you can add a new entry "new" or search for an existing entry by name "search"; "print" to view the current entries : press "q" to quit')
    select = input('Please select "new", "search", "print", or "q": ')
    while select != 'q':
        if select == 'new':
            new_phone()
        elif select == 'search':
            find_name()
        elif select == 'print':
                print_phonebook()        
def main():
    select()
            
main()

