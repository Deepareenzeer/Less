import random
#player
card1_py=random.randint(1,10)
card2_py=random.randint(1,10)
point_py=(card1_py+card2_py)%10

print("Point card1 player:",card1_py)
print("Point card2 player:",card2_py)
print("point Player:",point_py)


drawcard1=str(input("Draw card? [Y/N]:"))

if drawcard1 == "Y":
    card3=random.randint(1,10)
    point = (card1_py+card2_py+card3)%10
    print("Point player draw 1: ",point)
elif drawcard1 == "N":
    print("")
else:
    pass

#dealer
card1_dl=random.randint(1,10)
card2_dl=random.randint(1,10)
point_dl=(card1_dl+card2_dl)%10

print("Point card1 dealer:",card1_py)
print("Point card2:dealer",card2_py)

#calculater to finding winer
if point_dl>point_py:
    point_dl=("Dealer Winer!!")
elif point_dl<point_py:
    point_dl=("Player Winer!!")
else :
    point_dl == point_py
    point_dl=("Draw!!")
    
print(point_dl)










