# prime dictionary and add an element
foodDict = {'Spaghetti': 'Tangy Saucy Noodles'}

# function to add new elements to dictionary
def new_flavor():
    #get input
    newFood = input('Enter a new Food: ')
    if newFood in foodDict:
        confirm = input('That food is already in the dictionary, would you like to overwrite it? "y" or "n" ')
        if confirm.lower() == 'y':   # force check to lower case
            foodDict[newFood] = input('Enter a new flavor: ')
        else:
            print('You thought ', newFood,  'tastes like', foodDict[newFood])
    else:
        newTaste = input('How does it taste? ')
        foodDict[newFood] = newTaste
                
# search function    
def find_food():
    search = input('Please enter the food you are searching for: ')
    print(search, foodDict.get(search, ',that is not in the current dictionary'))  # get function to return value if key is found, otherwise return default value
    
# way to display the dictionary in a more 'reader friendly' manner  
def print_foodDict():
    for key, value in foodDict.items():
        print('Food:', key, 'Taste:', value)      
          
# define main    
def main():
    select = ''
    while select != 'q':
        select=input('Please select an option: "a" to add a new food, "f" to find a food, "p" to print the dictionary, or "q" to quit: ')
        if select == 'q':
           print('Come explore your flavors again soon!')
        elif select == 'a':
           new_flavor()
        elif select == 'f':
           find_food()
        elif select == 'p':
           print_foodDict()
        else:
           print('Invalid selection, please try again')
# call main
main()                      
