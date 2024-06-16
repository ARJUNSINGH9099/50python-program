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
