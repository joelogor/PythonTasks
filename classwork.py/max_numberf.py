def max_number(first_number,second_number,third_number):
    largest_number = first_number
  
    if second_number > first_number > third_number:
        largest_number = second_number 
    elif third_number > first_number > second_number:
        largest_number = third_number
        
    return largest_number
        
        
        
        
        
print(max_number(10,15,8))
