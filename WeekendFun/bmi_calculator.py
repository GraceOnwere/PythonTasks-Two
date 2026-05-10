#collect weight and height  calculate bmi and then display the bmi category
#
#to calculate bmi weight/(height * height)

#if bmi is less than 18.5 
#
#display underweight
#
#if bmi is between 18.5 and 24.9 
#
#display normal
#
#if bmi is betwen 25 and 29.9
#
#display overweight
#
#else display obese

weight = int(input('Enter your weight in kg: '))

height = float(input('Enter your height in meters: '))

bmi =round((weight/ (height * height)),1) 

if bmi < 18.5:

    print(f'Your BMI is {bmi} that means you are Underweight')

elif 18.5 <= bmi <= 24.9:

    print(f'Your BMI is {bmi} that means you are Normal')

elif 25 <= bmi <= 29.9:

    print(f'Your BMI is {bmi} that means you are Overweight')

else:

    print(f'Your BMI is {bmi} that means you are Obese')
