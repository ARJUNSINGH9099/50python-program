# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER
#  >= 30                 >=90          Hot and Humid
# >= 30                  < 90          Hot
# <30                   >= 90          Cool and Humid
# <30                     <90          Cool

temp=float(input("Enter the temprature:"))
hum=int(input("enter the humidity:"))

if temp>=30 and hum>=90:
    print("weather is hot and humid")
elif temp>=30 and hum<90:
    print("weather is hot")
elif temp<30 and hum>=90:
    print("cool and humid")
elif temp<30 and hum<90:
    print("cool")