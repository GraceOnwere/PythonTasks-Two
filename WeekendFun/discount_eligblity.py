#collect total bill and ask if the user is a member calculate discount and allocate message
#
#to calculate discounted bill = total bill - (total bill * (discount * 100))
#
#to allocate discount
#
#if total bill is greater than or equal to 1000 and is member is yes allocate 10% off 
#
#display discounted bill
#
#if total bil is greater than or equal to 1000 and is member is no allocate 5% off 
#
#display discounted bill
#
#else 
#
#display no discount your amount is less than 1000


total_bill = int(input('Enter your total bill: '))

is_member = input('Are you a member (yes/no): ')

if total_bill >= 1000 and is_member.lower() == 'yes':

    discount = 0.1

    discounted_bill = total_bill - (total_bill * discount)

    print(f'Your total bill is {total_bill} and your discounted bill is {discounted_bill}')

elif total_bill >= 1000 and is_member.lower() == 'no':

    discount = 0.05

    discounted_bill = total_bill - (total_bill * discount)

    print(f'Your total bill is {total_bill} and your discounted bill is {discounted_bill}')

else:

    print(f'Your total bill is {total_bill} and is less than 1000 so no discount allocated')

