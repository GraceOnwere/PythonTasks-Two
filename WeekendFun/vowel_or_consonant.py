#Ask user for a letter and check if its a vowel or consonant

user_input = input('Enter a letter (A-Z): ')

vowel = 'aeiou'

consonant = 'bcdfghjklmnpqrstvwxyz'

if user_input.lower() in vowel:

    print('Vowel')

elif user_input.lower() in consonant:

    print('Consonant')

else:

    print('Invalid input')
