# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

heads=int(input("enter the number of head:"))
legs=int(input("enter the number of legs:"))

if heads==legs/4:
    number_of_dogs=legs/4
    print("total number of dogs=",number_of_dogs)
elif heads==legs/2:
    number_of_chickens=legs/2
    print("total no of chicken is=",number_of_chickens)
else:
    print(" Error !! Not valid.....Exit")
   