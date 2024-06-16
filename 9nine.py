# 9. Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

angle_1=int(input("enter the angle_1:"))
angle_2=int(input("enter the angle_2:"))
angle_3=int(input("enter the angle_3:"))

if angle_1+angle_2+angle_3==180 and angle_1!=0 and angle_2!=0 and angle_3!=0:
    print("valid for triangle")
else:
    print("not valid")