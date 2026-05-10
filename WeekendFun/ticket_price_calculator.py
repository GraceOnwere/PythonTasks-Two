#collect age and allocate price of ticket
#
#if age is less than 5 
#
#display free
#
#if age is between 5 and 12 
#
#display $5
#
#if age is betwen 13 and 64
#
#display $12
#
#else display $8

age = int(input('Enter age : '))

if age < 5:

    print('Your ticket is free')

elif 5 <= age <=  12:

    print('Your ticket cost $5')

elif 13 <= age <= 64:

    print('Your ticket cost $12')

else:

    print('Your ticket cost $8')

