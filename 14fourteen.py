hour = int(input("Enter the hour: "))
min = int(input("Enter the minute: "))

minutAngle=min*6
hourAngle=(hour/12)*360              #

angle=abs(hourAngle-minutAngle)
if angle>180:
    angle=360- angle
print(angle)