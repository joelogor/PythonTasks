#Get father's age
#Get son's age
#
#Calculate number_of_years = absolute value of (father's_age - 2 * son's_age)
#
#Return number_of_years
#
#Call the function and print the result


father_age = int(input("Enter father's_age: "))
son_age = int(input("Enter son's_age: "))
    

def get_number_of_years(father_age, son_age):
    number_of_years = abs(father_age - (2* son_age))
    return number_of_years
    

number_of_years = get_number_of_years(father_age, son_age)
print("The father was twice as old as his son" + number_of_years + "years ago")
