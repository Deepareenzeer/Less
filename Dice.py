import random

dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)
sumr=(dice1+dice2+dice3)

print("If points between 3-10 is LOW")
print("If points between 11-18 is HIGHT")
print("-----------------------")

guess=str(input("Bet Hight or Low [H/L]:"))
num=int(input("Choose one dice (1-6) For BONUS!!:"))
print(F"The points is {dice1}+{dice2}+{dice3}={sumr}")

if (guess == "H" and sumr >= 11) or (guess =="L" and sumr<=10)  :
    print("You Win")
else :
    print("You Lose")
if (num==dice1 or num==dice2 or num==dice3) :
    print("BONUS!!")
else :
    print("No BONUS!!")
    
    
    
