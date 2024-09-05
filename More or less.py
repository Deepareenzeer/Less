print("----More or Less Game----")
import random
ran_num=random.randint(1,10)
Round=0

while Round != 5:
    
    next_num=random.randint(1,10)
    
    Round += 1
    Round1= input(f"รอบปัจจุบัน: {Round} เลขที่สุ่มได้: {ran_num} ทายว่าเลขต่อไป มากกว่า (M) หรือ น้อยกว่า (L) :")
    print(f"Random Number:{next_num}")
    
    if (next_num > ran_num and Round1 =="M") or (next_num < ran_num and Round1 =="L") or (next_num == ran_num):
        print("คำตอบของคุณ:ถูกต้อง")
        print("-----------------------")
        ran_num=next_num
    else:
        print("คำตอบของคุณ:ไม่ถูกต้อง")
        print("-----------------------")
        break
if Round <=5:
    print(f"คุณทำได้ {Round} รอบ คุณแพ้!!")
    print("-----------------------")
else:
    print(f"คุณทำได้ {Round} รอบ คุณชนะ!!")
    print("------------------------")
