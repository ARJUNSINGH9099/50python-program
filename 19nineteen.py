#  Write a menu driven program - 1.cm to ft� 2.kl to miles� 3.usd to inr� 4.exit

user_input=input(''' hi!! Welcome to my page.
                 what would you like to convert.
                 
                 1.Centimeter to Inch
                 2.Kilometer to miles
                 3.USD to INR
                 4.Exit
                 ''')


if user_input=="1":
    cm=float(input("Enter your value in cm:"))
    inch=cm*0.393701
    print("your value in inches is ",inch)

elif user_input=="2":
    km=float(input("enter the value in km:"))
    miles=km*0.621371
    print("your values in miles" ,miles)
elif user_input=="3":
    usd=float(input("Enter the value in usd:"))
    inr=usd*83.2124
    print("your INR value is",inr)
else:
    print("Exit")

