import random

user_id = "admin"
password = 12345

u_id = input("Enter the User_id: ")
p = int(input("Enter the pasword: "))

if(u_id == user_id and p == password):

    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    user_captcha = int(input("Enter the captcha from user: "))

    if(user_captcha == captcha):
        print("Login Successful.")
    else:
        print("Captcha doesn't match.")

else:
    print("Invalid User_id or Password")