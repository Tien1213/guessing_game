import random
b = random.randint(1, 101)

attempt = 0

while attempt < 100:
    a = int(input("enter a number:"))
    attempt = attempt + 1

    if attempt == 100:
        print("Out of Attempt!!! " + "The Number is: "+ str(b))

    elif a > b:
        print("lower!! " + "You have " + str(100 - attempt) + " attempts left")

    elif a < b:
        print("higher!! " + "You have " + str(100 - attempt) + " attempts left")

    elif a == b:
        print("correct!! The Number is: " + str(b))
        break

