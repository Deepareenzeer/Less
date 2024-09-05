subjects=["OS","DB","DS"];total_credits=0;total_points=0

for subjects in subjects:
    credits=float(input(f"หน่วยกิจของวิชา {subjects}:"))
    grade=float(input(f"วิชา {subjects} ได้เกรด:"))
    total_credits += credits
    total_points += grade*credits
    
GPA=total_points/total_credits
print(f"GPA={GPA}")