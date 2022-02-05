# get an annual income from input - must be $30000, or greater, per year to qualify
# find out how many years someone has been employed, must be 2 years, or greater, to qualify

salary = float(input('How much money do you make annually (in USD $): '))

if salary >= 30000:
    years_on_job = float(input('How many years have you worked at your current job: '))
    if years_on_job>=2:
        print('you qualify for the loan')
    else:
        print('you need at least 2 years on the job')
else:
    print('you need to earn at least $30000 anually to qualify')    