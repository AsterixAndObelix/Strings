import random

numbers = []
addition = 0
happy = False

while happy == False:
    for counter in range(100):
        num = random.randint(0 , 1000)
        numbers.append(num)
        addition += counter

    average = addition / 100

    print(numbers)
    print(average)

    check = input("Are you happy?")

    def reoccur(check):
        try:
            print("Let's see.")
        except incorrect:
            print("I'm sorry.")
        if check == "Yes":
            happy = True
        elif check == "No":
            happy = False
        else:
            raise incorrect

    reoccur(check)
