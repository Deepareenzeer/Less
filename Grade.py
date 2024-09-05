point=int(input("Enter your score:"))

if point >= 80:
    grade=("A")
elif point >=70:
    grade=("B")
elif point >=60:
    grade=("C")
elif point >=50:
    grade=("D")
elif point <50:
    grade=("F")
else:
    pass

print("Your grade is:",grade)