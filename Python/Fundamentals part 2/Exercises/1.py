age = int(input("Enter your age: "))
if age < 13:
    print("Child.")
elif age >= 13 and age <= 18:
    print("Teenager")
elif age > 18:
    print("Adult.")
else:
    print("Invalid input")