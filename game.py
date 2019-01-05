import random
b = random.randint(1, 101)

attempt = 0

while attempt < 31:
    a = int(input("enter a number:"))
    attempt = attempt + 1

    if a > b:
        print("lower!!")


    elif a < b:
        print("higher!!")


    elif a == b:
        print("correct!!")
        break



