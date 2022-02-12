# employee number and hours looping program

def totalEmpHours():     # this is creating a function <with NO parameters>
    totalEmpHours = 0    # set the variable to 0

    empNum = input('Enter the employee number [enter "0000" to exit the program]: ')  # ask for user to input the empNum value
    while empNum != '0000':  # we set the loop to run as long as the empNum is not equal to '0000'

        empHour = float(input('Enter the employee hours: '))   # we know that as long as 0000 wasn't entered above there will be hours for the employee and we want a float in case there are irrational hours
        totalEmpHours += empHour     # ACCUMULATOR
        empNum = input('Enter the next employee number ["0000" to exit]: ')
    print('Total employee hours ---> ', totalEmpHours)        

totalEmpHours()
