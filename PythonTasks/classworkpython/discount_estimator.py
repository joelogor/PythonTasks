'''Enter amount and print the discount
 Puerchase between 1000 and 10000 receives a 5% discount
 Puerchase between 10000 and 50000 receives a 5% discount
 Puerchase between 50000 and and above receives a 5% discount
int spend = 10000'''

total_purchases = int(input("Enter total amount spent: "))

if total_purchases >= 1000 and total_purchases <= 10000:
	percentage_discount = (5/100) * total_purchases
	discount_amount = percentage_discount - total_purchases
	print("The Percentage discount ", percentage_discount)

elif total_purchases > 10000 and total_purchases <= 50000:
	percentage_discount = (10/100) * total_purchases
	discount_amount = percentage_discount - total_purchases
	print("The Percentage discount ", percentage_discount)

elif total_purchases > 50000:
	percentage_discount = (20/100) * total_purchases
	discount_amount = percentage_discount - total_purchases
	print("The Percentage discount ", percentage_discount)

elif total_purchases < 1000:
	print("No discount")



