for number in range (1, 10,1):
    print(number, end="|\t")
    for count in range(1, 10,):
        multiplication = number * count 
        print(f"{multiplication:>3}", end = "   ")    
    print()
