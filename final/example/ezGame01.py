direction = ''
while direction != 'q':
    print('\n', 'You see portals that lie to the North "n", South "s", East "e", and West "w".')
    direction = input('Which portal do you choose? "n", "s", "e", or "w"? press "q" to quit.')
    
    if direction.lower() == 'n':
        if direction: 
            pass
        else: pass
        

    elif direction.lower() == 's':
        if direction: pass
        else: pass
        
    elif direction.lower() == 'e':
        pass
    
    elif direction.lower() == 'w':
        pass
    
    elif direction.lower() == 'q':  # quit
        print('You have chosen to quit the game.')
    
    else:
        print(
            'You have chosen an invalid direction, please choose "n", "s", "e", "w", or "q".')  # invalid direction
            
            