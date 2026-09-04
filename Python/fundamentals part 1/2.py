print("*****Welcome to the Calculator*****")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choose = int(input("choose 1 for addition\n" \
                   "choose 2 for Subtraction \n"
                   "choose 3 for Multiplication\n"
                   "choose 4 for division\n"))

match choose:
    case 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    case 2:
            print(f"{num1} - {num2} = {num1 - num2}")
    case 3:
            print(f"{num1} * {num2} = {num1 * num2}")
    case 4:
            if num2 == 0:
                print("cannot be divide by zero")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
    case _:
            print("Invalid choice")
'''task was easy i made my own modification with in my knowledge about python'''