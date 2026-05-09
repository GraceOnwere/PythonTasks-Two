#Collect 2 numbers
#
#Collect an arithemetic operator(+, -, * and /)
#
#perform the opeation based on the operator

#if the operator is + add the numbers
#
#if the opeartor is - subtract the numbers
#
#if the operator is * multiple the numbers
#
#if the operator is / divide the numbers
#
#for division operation handle the zero division error

import sys

title = '\n\tWATCH ME PERFORM MAGIC!!!'

print(f'{title}')

user_input_one = int(input('\nEnter first number: '))

user_input_two = int(input('\nEnter second number: '))

arithemetic_operator = input('\nEnter an arithemetic operator(+, - ,*, /): ')


match(arithemetic_operator):

    case '+':

        operation = user_input_one + user_input_two
        print(f'The addition of {user_input_one} and {user_input_two} is {operation}')

    case '-':
        operation = user_input_one - user_input_two
        print(f'The subraction of {user_input_one} and {user_input_two} is {operation}')

    case '*':

        operation = user_input_one * user_input_two
        print(f'The multiplication of {user_input_one} and {user_input_two} is {operation}')

    case '/':
        if user_input_two == 0:
            print('Invalid operation')
            sys.exit()
        operation = user_input_one / user_input_two
        print(f'The division of {user_input_one} and { user_input_two} is {operation}')




    


        


