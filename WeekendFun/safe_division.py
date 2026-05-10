#Collect 2 integers
#
#perform division operation if second integer is not equal to zero
#
#else display cannot divide by zero
#




user_input_one = int(input('Enter first number: '))

user_input_two = int(input('Enter second number: '))

if user_input_two != 0:

    division = user_input_one / user_input_two
    
    print(f'{user_input_one} divided by {user_input_two} is {round(division,2)}')

else:

    print('Cannot divide by zero')

