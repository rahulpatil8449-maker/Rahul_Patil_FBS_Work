user_id = input("Enter the userid of the user: ")
password = int(input("Enter the password: "))

uid = 'uname'
p = 12345

if(user_id == uid and password == p):
    print("The UserId and Password is valid.")
else:
    print("The UserId and Password is invalid.")