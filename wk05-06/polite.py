#ask for user name and title & create a polite greeting
#this is a value-returning function (returns name & title)
def ask_name_title():
    name=input('Enter your name')
    title= input('What is your title?')
    return name, title

#this is a void function that prints
def greeting(user_name, user_title):
    print('Hello,', user_title, user_name)    
    
def main():
    user_name1, user_title1 = ask_name_title()
    greeting(user_name1, user_title1)

main()
