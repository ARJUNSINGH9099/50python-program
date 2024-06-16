# from datetime import datetime
# class Person:
    
    
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=datetime.strptime(date_of_birth,"%Y-%m-%d")
        
#     def calculate_age(self):
#         today=datetime.today()
#         age=today.year-self.date_of_birth.year
#         if today.month<self.date_of_birth.month or(today.month==self.date_of_birth.month and today.day<self.date_of_birth.day):
#             age-=1
#         return age



# a=Person("Arjun","Deoband","1994-11-29")
# print("name is:",a.name)
# print("City is:",a.country)
# print("date of birth is:",a.date_of_birth)

# print(f"age:{a.calculate_age()} years")

    

# write a Python program to swap first and last element of the list.
# approch:1
# by unpacking
# l=[1,2,3,4,5]

# s,*m,e=l
# l=e,*m,s
# print(l)

# approch:2

# by slicing
# l=[1,2,3,4,5]

# print(l[-1:]+l[1:-1]+l[:1])

# approch:3
# l=[1,2,3,4,5]

# first=l.pop(0)
# last=l.pop(-1)
# l.insert(0,last)
# l.append(first)
# print(l)

# approch:4

# l=[1,2,3,4,8]
# get=l[-1],l[0]

# l[0],l[-1]=get
# print(l)



