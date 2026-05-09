#Collect password
#
#Check the password length
#
#if the password is less than or equal to 10 
#display medium
#
#if the pass word is less than 6 
#display weak
#
#if the password is less than one 
#display invalid


input_collector = input('Enter your password: ')

if 6 <= len(input_collector) <= 10:

    print('Your password Strength is Medium')

elif len(input_collector) < 6:

    print('Your password Strength is Weak')

elif len(input_collector) > 10:

    print('Your password Strength is Strong')

elif len(input_collector) < 1:

    print('Your password Strength is invalid')



