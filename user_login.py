import os

title = "USER LOGIN"
print(title.center(50))
print("to login, enter the name and password you used to register.")

Lname = input("Enter your name:\t")
Lpassword = input("Enter your password:\t")

if os.path.exists(Lname+Lpassword+".txt"):
   user_file = open(Lname+Lpassword+".txt","a")
   content_title = "Welcome "+ Lname
   content_title.upper()
   user_file.write(content_title.center(50))
   content = " Login was successful, you are welcome"
   user_file.write(content)
   
   user_file = open(Lname+Lpassword+".txt")
   print(user_file.read())

else:
    print("Oops!,looks like you have not registered yet")
    


