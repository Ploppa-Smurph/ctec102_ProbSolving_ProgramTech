'''
1. Write Program to create dictionary of US as Keys and their Capitals as Values.
2. Program should randomly quiz the user 5 times on the State Capitals. 
3. Keep count of Correct and Incorrect
4. Print out a total at the end of the 5 questions. 
'''
### made a constant for the number of times to run the quiz
NUM_STATES = 5

##########################################################################
#  Main Function    
#########################################################################
def main():
    state_caps = state_cap_dictionary()

##########################################################################
#    Initialize Variables for Correct and Incorrect Answers
#########################################################################
    cor = 0
    incor = 0

##########################################################################
#   'for' Loop to iterate over dictionary and randomly select key and value item 
##########################################################################
    for count in range(NUM_STATES):
        
##########################################################################
#    Get random element and remove it from the dictionary
#########################################################################
        state, capital = state_caps.popitem()

##########################################################################
#    Ask user for answer
#########################################################################
        print('What is the capital of', state, '?', end='')
        response = input()

##########################################################################
#    Compare user input to correct dictionary answer -- convert to lowercase using '.lower()'
#########################################################################
        if response.lower() == capital.lower():
            cor += 1
            print('Correct!')
        else:
            incor += 1
            print('Incorrect!')
            print('The correct answer is', capital)

#####################################################################
#   Display Total Correct and Incorrect Answers
#######################################################################
    print('You got', cor, 'correct answers')
    print('and you got', incor, 'incorrect answers')


##########################################################################
#    Initialize Dictionary containing US States and their Capitals
#########################################################################
def state_cap_dictionary():    
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    return capitals

##########################################################################
#   Call the main() function   
#########################################################################
main()
