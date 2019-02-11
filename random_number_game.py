import random
random_number = random.randint(0, 10)
print(random_number)
guess = None
while random_number != guess:
    guess = int(input("Welcome to guessing game!!!enter a number between 1 to 10 \n "))
    if guess < random_number:
        print("ugh your number is too low")
    elif guess > random_number:
     print("your number is too high gentleman")
    else:
        print("congratulations you won!!!!!!!!!!")
        print(random_number)
        var = input("do you want to play anymore or  not,please select between ""y/n ")
        if var == "y":
            # random_number = random.randint(0, 20)
            print(random_number)
            guess = None

        else:
            print("thanks for playing")
            break