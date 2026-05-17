from pybank import *





message = """ 1. Register
2. Login
3. Calculate
4. Apply Interest
5. Summary
6. Exit"""


while True:
    user_input = input(message)
    match user_input:
        case "1":
            email = input("Enter email:")
            password = input("Enter password:")
            if validate_email(email) and is_strong_password(password):
                print("registration succesful")
            else:
                print("Registration failed")  
        case "2":
            email = input("Enter email:")
            password = input("Enter password:")
            if validate_email(email) and is_strong_password(password):
                print("Login succesful")
            else:
                print("Login failed")              
        case "3":
            amount = float(input("Enter amount or 0:")) 
            while amount !=0
                transactions.append(amount)
                amount = float(input("Enter amount or 0:")) 
            total_transaction =     
                
                       
