# Q tuple with first and last element
from operator import itemgetter

# element = int(input("Enter the number of elements you want to add: "))
mylist = ['ram', 'shyam', 'nilesh', 'darshan', 'ashok']
# for i in range(element):
#   mylist.append(input("Enter the element: "))

mytuple = itemgetter(0, -1)(mylist)

mytuple = (mylist[0],mylist[-1])

print(mylist)  
print(mytuple)
print(type(mytuple))
# append = add element at the last position

# insert = add element at the specified position  

# How to take list element as a input using split method
