# Get the first_score, second_score, and third_score

# Calculate the average_of_scores = (first_score + second_score + third_score) / 3

# Compare the average score and return the corresponding grade 
# using a match-case statement based on the grading system

# Call the function
# Print the returned grade

first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))


def get_grade(first_score, second_score, third_score):
    average_score = (first_score + second_score + third_score)/3
    
    if average_score >= 90 and average_score <= 100:
        grade = "A"
    elif average_score >= 80 and average_score < 90:
        grade = "B"
    elif average_score >= 70 and average_score < 80:
        grade = "C"
    elif average_score >= 60 and average_score < 70:
        grade = "D"
    elif average_score >= 0 and average_score < 60:
        grade = "F"
   
    return grade
    
print(get_grade(first_score, second_score, third_score))
