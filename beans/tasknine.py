seconds = int(input('Enter number in seconds:'))
hour = seconds//3600
remaining_seconds = seconds%3600
minute = remaining_seconds//60
remaining_seconds = remaining_seconds//60

print(hour, ":" , minute , ":" , remaining_seconds)
