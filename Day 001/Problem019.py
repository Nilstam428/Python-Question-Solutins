# Q. number of unique combination on two dice

#for getting number of unique combination on two dice we can perform loop for getting values

count = 0
for i in range(1, 7):
    print(end="")
    for j in range(1, 7):
        count += 1
        print(f"({i},{j})")

print("Number of unique combinations:", count) 

