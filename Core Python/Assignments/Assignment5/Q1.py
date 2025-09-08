user_id = "admin"
password = "12345"

for attempt in range(1, 4):
    u_id = input("Enter the User_id: ")
    p = input("Enter the password: ")

    if(u_id == user_id and p == password):
        print("Login Successfull.")
        break

    else:
        print("Invalid Credentials.")
        if(attempt < 3):
            print(f"{3 - attempt} attempts left.")
        else:
            print("Too many invalid attempts.")