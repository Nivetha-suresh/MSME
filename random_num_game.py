import random

a=random.randint(1,10)
print(a)
for i in range(3):
    b=int(input("enter number(between 1-10)"))
    if b<1 or b>10:
        break
    if a==b:
        print("HURRY"+"YOU WON")
        break
    else:
        print("not equal"+"better luck next time")
