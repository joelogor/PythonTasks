'''User enter password
password length less than , 8 print 'very weak'
password length 8 , print 'weak'
password length between  8 and 16 , print 'strong'
password length above 16, print 'very strong'''


password = input("Create your password: ")
password_strength = len(password)

if (password_strength < 8):
	print("your password is weak")
 
elif (password_strength >= 8 and password_strength < 16):
	print("your password is strong")
	
elif (password_strength > 16):
	print("your password is very strong")
