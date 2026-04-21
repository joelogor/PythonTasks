#Simple interest

principal = int(input('Enter Principal:'))
rate = int(input('Enter Rate:'))
time = int(input('Enter Time:'))

interest = (principal*rate*time)/100

totalamount = principal+interest

print('The simple interest is' , interest , 'and the total amount is ' , totalamount)
