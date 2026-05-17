#Get year input from user
#
#Determine whether the year is a leap year using these rules:
#   - Divisible by 4 but not by 100, OR
#   - Divisible by 400
#
#Assign "Leap year" or "Not Leap year" accordingly
#Return the result
#
#Call the function and print the output

year = int(input("Enter year: "))

def check_if_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = "a Leap year"
    else:
        result = "Not a Leap year"

    return result

check_year = check_if_leap_year(year)

print(check_year)
