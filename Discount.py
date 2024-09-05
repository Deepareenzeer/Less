money=float(input("Enter total amount:"))
member=str(input("Enter member? [Y/N]:"))

if member == ("Y") and money>=5000:
    rate=money*0.2
    discount=(money-rate)
    
elif member ==("N") and money>=5000:
    rate=money*0.1
    discount=(money-rate)
    
elif member == ("Y") and money<5000:
    rate=money*0.05
    discount=(money-rate)
    
elif member == ("N") and money<5000:
    rate=money*0.05
    discount=(money-rate)
    
else:
    pass

print("Discount:",rate)
print("Net money:",discount)
    
    
    