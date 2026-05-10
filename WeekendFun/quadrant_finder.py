#collect 2 integers x and y and allocate which quadrant it is
#
#if x is greater than 0 and y greater than 0 
#
#display Q1
#
#if x is less than 0 and y greater than 0
#
#
#display Q2
#
#if x is less than 0 and y is less than 0
#
#display Q3
#
#if x greater 0 and y is less than 0 
#
#display Q4
#
#if x and y is equal to 0
#
#display Origin
#
#if y is equal to 0 and x is not 
#
#display X axis
#
#if x is equal to 0 and y is not 
#
#display Y axis

number_one = int(input('Enter first number: '))

number_two = int(input('Enter second number: '))

if number_one > 0 and number_two > 0:

    print('Q1 (First Quadrant)')

elif number_one < 0 and number_two > 0 :

    print('Q2 (Second Quadrant)') 

elif number_one < 0 and number_two < 0:

    print('Q3 (Third Quadrant)')  

elif number_one > 0 and number_two < 0:

    print('Q4 (Fourth Quadrant)') 

elif number_one == 0 and number_two == 0:

    print("Origin")

elif number_two == 0 and number_one != 0:

    print('X-axis')

elif number_one  == 0 and number_two != 0:

    print('Y-axis')
