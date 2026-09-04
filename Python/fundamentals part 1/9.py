PA = input("Enter principle amount: $")
R =  input("Enter Rate of interest: ")
T =  input("Time taken(in years): ")
SI = (float(PA)*float(R)*float(T))/100
print(f"Simple Interest: {round(SI,2)}")