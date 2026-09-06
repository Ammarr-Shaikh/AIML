while True:
        n = int(input("Enter a number: "))
        if n > 0:
            print("it is positive")
        elif n <0:
            print("it is negative")
        else:
            print("number is zero")
        user = input("Continue or Quit: ")
        if user == "quit":
             break