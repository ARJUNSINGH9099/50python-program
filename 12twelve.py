# 12. Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

# v=pi*r*r*h  wher pi=3.14

radius=float(input("enter the value of radius:"))
height=float(input("enter the value of height:"))

vol_cylinder=3.14*(radius**radius)*height
print("your cylinder volume is ",vol_cylinder)

cost=vol_cylinder/1000*40
print("your cost is ","%0.2f"%cost)