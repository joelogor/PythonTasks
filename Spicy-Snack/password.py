#Collect the password input
#
#Determine password_strength by evaluating the password length 
#according to the specified conditions
#
#Call the function
#Print the result (password strength)

password = input("Enter your password: ")

def check_password_strength(password):
    if len(password) >= 6 and len(password) <= 10:
        password_strength = "medium"
    elif len(password) >= 1 and len(password) < 6: 
        password_strength = "weak"
    elif len(password) > 10:
        password_strength = "strong"
    elif len(password) < 1:
        password_strength = "invalid"
    
    return password_strength

password_strength = check_password_strength(password)
print(password)
