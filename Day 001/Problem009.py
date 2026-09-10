# Q insert element at particuler index (without insert method)


l1 = [1, 2, 3]
# l1[2] = "jp"
l1.insert(1, "jd")
print(l1)

# 1. list = mutable data type (value change )

l1 = input("enter elements in list : ").split()

l2 = l1.copy()
ins = int(input("Enter the index where you want to ienter the element: "))
value = int(input("Enter the value you want to insert: "))
l1[ins] = value

#adjust the rest of the list 
for i in range(ins+1, len(l1)):
    l1[i] = l2[i-1]
l1[-1] = l2[-1]
print("Modified List :", l1)


# Q how to add element in  list at last position.

# element = int(input("Enter number of elements in list :"))
# l1 = []
# for i in range(element):
#     value = int(input("enter value : "))
#     l1.append(value)

# # l2 = l1.copy()

# # ins = int(input("enter a index :"))
# # value = input("enter a value :")
# # l1[ins] = value

# # print(l1)

# # for i in range(ins + 1, len(l1) + 1):
# #     l1[i] = l2[i - 1]

# # print(l1)


# element = int(input("Enter number of elements in list: "))
# l1 = []
# for i in range(element):
#     value = int(input("Enter value: "))
#     l1.append(value)

# # Create a copy of l1
# l2 = l1.copy()

# # Modify the value at the specified index
# ins = int(input("Enter an index: "))
# value = int(input("Enter a value: "))  # Assuming you're inputting an integer
# l1[ins] = value

# # Adjust the rest of the list
# for i in range(ins + 1, len(l1)):
#     l1[i] = l2[i - 1]
# l1[-1] = l2[-1]

# print("Modified list:", l1)

