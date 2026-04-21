principal = int(input('Enter principal:'))
rate = int(input('Enter Annual Interest Rate:'))

time = int(input('Enter Duration:'))

rate = rate/(12/100)
time = time*12

result = rate

result =  principal*(rate*(1+rate)**time)/(((1+rate)**time)-1)

print(result)

