user_input = int(input("Enter a number: "))

for row in range(user_input + 1 ,1,-1):
    for column in range(row -1, 0,-1):
        print(column,end= " ")
    print()
