import random

#pass_count = 0
def generate_two_numbers ():
    
    number_one = random.randint(1,10)

    number_two = random.randint(1,10)

#    if number_one > number_two:
#
#        question = (f"{number_one} - {number_two}")
#
#        return (question)

#    else:
#    return (f"{number_two} - {number_one}")

    return number_one,number_two
#    def collect_user_answer ():

#        answer = number_one - number_two
#
#        user_input = int(input("Enter your answer: "))
#
#        if answer == user_input: 
#            return "correct"
#
#        else: 
#
#            user_input = int(input("Enter your answer: "))
#
#            if user_input != answer:   
#                return "wrong"
#
#        return "correct"
#
#    collect_user_answer()

        
    
#    def ask_the_user_ten_times():
#        pass_count = 0
#        correct_answer = collect_user_answer()
#
#        if correct_answer == "correct":
#            
#            pass_count = pass_count + 1
#       
#        for number in range( ):
#            generate_two_numbers()
#
#        return (f"You got {pass_count} out of 10 questions")
#
#    ask_the_user_ten_times()
#        
#           
#        print(pass_count)   
#
#    return collect_user_answer()


                


print(generate_two_numbers())

#print(collect_user_answer())
