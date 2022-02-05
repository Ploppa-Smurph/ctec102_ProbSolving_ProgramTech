# convert a given amount of seconds into hours, minutes, and seconds
# ex: 400 seconds is 0 hours,  6 minutes, 40 seconds
# 60 seconds = 1 minute, 60*60 seconds = 1 hour
print('This Sophisticated Program will take the amount of seconds you enter and display them as Hours, Minutes, and Seconds. Enjoy!')
seconds = int(input('Please enter the amount of seconds to convert (use a whole number): '))
hours = seconds//3600
remainder1 = seconds%3600
minutes = remainder1//60
remainder2 = remainder1%60
print(hours, ' hours, ', minutes, ' minutes, ', remainder2, ' seconds')