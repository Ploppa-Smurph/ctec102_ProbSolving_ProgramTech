# bug collector collects bugs every day for 1 week 
# keep a total of all bugs collected and display at end
print("Welcome to the World's Greatest Interactive Digital Weekly Bug Count Tally")

#create accumulator bugTotal and set to value 0
bugTotal = 0

#for each day of week (7 days)
for day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:

#input # of bugs caught that day
    bugs = int(input('How many bugs did you hunt down on '+ day +'?'))

#add bugs to bugTotal
    #bugTotal = bugTotal + bugs
    bugTotal += bugs
    
# @ end display total
print('over the last week you collected a total of', bugTotal, 'bugs.')
