pass_count = 0

fail_count = 0

for number in range(15):

    user_input = int(input("Enter a number: " ))

    if user_input >= 45:
        pass_count+=1
    else:
        fail_count+=1

print(f"{pass_count} students passed\n{fail_count} students failed")
