#collect 3 integers
#
#declare and initialize the first number as the largest
#
#if second number is greater than largest
#
#the second number becomes the new largest
#
#if the third number is greater than the largest 
#
#the third number becomes the new largest
#
#display the largest


user_input_one = int(input('Enter first number: '))

user_input_two = int(input('Enter second number: '))

user_input_three = int(input('Enter third number: '))

largest = user_input_one

if user_input_two > largest:

    largest = user_input_two
    
if user_input_three > largest:

    largest = user_input_three
    
print(f'{largest} is the largest')



