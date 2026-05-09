#Collect first score (0-100)
#
#Collect second score (0-100)
#
#Collect third score (0-100)
#
#sum the score collected
#
#average is equal to the sum of scores divided by 3
#
#allocate grade based on this grading system
#
#90 <= score <= 100 'A'
#80 <= score < 90 'B'
#70 <= score < 80 'C'
#60 <= score < 70 'D'
#0 <= score < 60 'F'


title = '\tTHE AVERAGE OF 3 SCORES CALCULATOR!!!'

print(f'{title}')

score_counter = 0

sum_of_scores = 0

while score_counter <= 2:

    score_counter +=1

    input_collector = int(input('\nEnter score: '))
    
    sum_of_scores += input_collector


average = sum_of_scores / score_counter


if 90 <= average <= 100:

    print(f'\nThe average of the {score_counter} scores is A')

elif 80 <= average < 90:

    print(f'\nThe average of the {score_counter} scores is B')

elif 70 <= average < 80:

    print(f'\nThe average of the {score_counter} scores is C')

elif 60 <= average < 70:

    print(f'\nThe average of the {score_counter} scores is D')

elif 0 <= average < 60:

    print(f'\nThe average of the {score_counter} scores is F')

