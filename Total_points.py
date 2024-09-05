subjects=['OS','DB','DS']
total_points=0
for subjects in subjects:
    Name_sj=subjects
    for i in range(3):
        points=float(input(f"คะแนนสอบของวิชา {Name_sj} ครั้งที่ {i+1}:"))
        total_points+= points
    print(f"วิชา{Name_sj}ได้คะแนนรวม={total_points}")
    print("------------------------------")
        