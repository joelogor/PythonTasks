def exchange_converter(dollar):
    dollar = 0
    naira = 0
    if dollar>=1:
        naira = dollar*1550
        return naira
        
        
print(exchange_converter(2))        
