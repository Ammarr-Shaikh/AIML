Temperature = input("Enter temperature in celsius: ")
print(type(Temperature))
# To be taken in string and convert to float
fahrenheitTemp = ((float(Temperature)*(9/5)) + 32)
print(f"Temperature in Fahrenheit: {round(fahrenheitTemp,2)} ")
print(type(fahrenheitTemp))