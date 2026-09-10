# use these list functions
# 1. append()
# 2. insert()
# 3. remove()
# 4. clear()
# 5. count()
# 6. reverse()
# 7. pop()
# 8. slicing


l1 = [1, 20, 30, 30, 20, 30, 40]
l1.append(50)
print(l1)
l1.insert(1, 10)
print(l1)
l1.remove(40)
print(l1)
# l1.clear()
print(l1.count(30))
l1.reverse()
print(l1)

l1.sort()
print(l1)


l1.pop()
print(l1)

print(l1[4:])