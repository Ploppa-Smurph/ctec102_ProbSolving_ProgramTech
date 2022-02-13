# create haunted house with room  
# keep user in menu until the choose to leave - input validation
print('Welcome to my Haunted House. You will be given a choice of rooms to explore below:')
print()



roomNum = -99   # prime the loop with an unlikely number
totalHours = 0

print('1 - the Living Room')
print('2 - the Dining Room')
print('3 - the Kitchen')
print('4 - the Upstairs Bedroom')
print('5 - the Basement')
print("6 - I'm so SCARED right now I need to QUIT")
print()

while roomNum < 1 or roomNum > 6:
    while roomNum != 6:
        # each room takes 1 hour to explore; 'accumulate' that data
        totalHours += 1 
    
# user will 'input' a room to explore
        roomNum = int(input('Please enter the room number you would like to explore: '))
        print()

# 'output' will be a spooky descripton
        if roomNum == 1:
            print('The Living Room of the house is dusty and looks like some marinara sauce was thrown on the wall. Why would someone throw marinara on the wall?')
            print()
        elif roomNum == 2:
            print('The Dining Room has a turkey carcase on the table. Flies are buzzing around the room and you feel queasy from the smell.')    
            print()
        elif roomNum == 3:
            print('The Kitchen of the house has a very large assortment of knives and well used cleavers strewn across the counters and floor.')
            print()
        elif roomNum == 4:
            print('The stairs creek as you approach the Upstairs bedroom. When you make your way towards the center of the room the door slams shut behind you! You frantically search for a way to get out')
            print()
        elif roomNum == 5:
            print("Awww, are you certain you want to go down the basement? You steady your hand and start making your way down the stairs when you hear a familiar humming, a refridgerator? Yes, as you make your way down into the basement you notice a newish clean refridgerator on the far wall. The refridgerator is purring along and seems to beckon for you to open it's door")
            print()
        elif roomNum == 6: 
            print('I hope you will survive this ordeal')           
            print()
# when user leaves output hour total along with parting statement
            print('Amazingly you survived', totalHours, 'hours in the Haunted House. Until next time')
