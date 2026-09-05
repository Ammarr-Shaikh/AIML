username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "pass":
    print("login successful")
# elif username != "admin" and password != "pass":
#         print("login failed")
elif username != "admin":
    print("wrong username")
else:
    print("Wrong password")

