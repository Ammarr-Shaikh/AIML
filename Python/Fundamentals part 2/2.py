while True:

    user = input("Do you wanna continue")
    if user =="quit":
        break
    else:
        n = int(input("Enter a number: "))
        if n > 0:
            print("it is positive")
        elif n <0:
            print("it is negative")
        else:
            print("number is zero")