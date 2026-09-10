# Q add element in tuple

mytuple = (1, 2, 3, 4)
new_element = int(input("Enter number you want to add: "))  # convert input to int
newtuple = mytuple + (new_element,)   # add as tuple with one element

print("Original:", mytuple)
print("New:", newtuple)
print(type(new_element))


# Remove duplicates

li = (3,5,2,3,2)
l1 = set(li)
l1 = tuple(l1)
print(l1)