user_input = int(input("Enter a number: "))

for row in range(1,user_input + 1):
    for column in range(row):
        print("*",end= " ")
    print()
