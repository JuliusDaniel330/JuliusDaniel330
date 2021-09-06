title = "REGISTRATION"
print(title.center(50))
print("In order to register, enter your name and password")

name = input("Name:\t")
password = input("Password:\t")

try:
    user_file = open(name + password + ".txt", "x")

except FileExistsError:
    print("The name " + "\"" + name + "\"" + " with password " + "\"" + password + "\"" + " has already been registered")
else:
    print("Registration successful")