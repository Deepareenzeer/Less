Book1=int(input("Book1 Price:"))
Book2=int(input("Book2 Price:"))
Book3=int(input("Book3 Price:"))
sum=Book1+Book2+Book3



if  Book1<Book2<Book3:
    min=Book1
elif Book2<Book1<Book3:
    min=Book2
elif Book3<Book2<Book1:
    min=Book3
else:
    pass


    
print(F"Summary:{sum}")
print(F"Min Price:{min}")
print(F"Real Price:{sum-min}")


