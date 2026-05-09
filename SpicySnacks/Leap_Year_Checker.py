#Collect year
#
#Check if the year is a leap year
#
#a leap year is divisible by 4 but not 100 and if the year is divisible by 400
 
input_collector = int(input('Enter a year: '))

if input_collector % 4 == 0 and input_collector % 100 != 0:

    print(f'{input_collector} is a leap year')

elif input_collector % 400 == 0:

    print(f'{input_collector} is a leap year')    

else:

    print(f'{input_collector} is not leap year')




