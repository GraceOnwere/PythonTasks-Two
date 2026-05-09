#Collect first age input (1-80)
#
#Collect second age input(1-80)
#
#Calculate the years ago the fathers age was twice the son's age
#
#let years ago would be = (sons age * 2) - fathers age
#
#check for negative years and covert to postive because time is a non negative quantity
#



import sys

title = '\tWELCOME TO THE TWICE-AS-OLD AGE CALCULATOR!!!'

print(f'{title}')

fathers_age = int(input('\nEnter Father\'s age (1-80): '))

sons_age = int(input('Enter Son\'s age (1-80): '))

if (fathers_age > 80):

    print('Father\'s age is greater than 80 try again')
    
    sys.exit()

elif (sons_age > 80):

    print('Son\'s age is greater than 80, IMPOSSIBLE try again!')
    
    sys.exit()

years_ago = (sons_age * 2) - fathers_age

if years_ago < 0:

    print(f'{abs(years_ago)} years from now, You would be twice as old as your son')

elif years_ago == 0:

    print(f'You are currently twice as old as your son')

else:
    print(f'{years_ago} years ago You were twice as old as your son')
