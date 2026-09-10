# Q Write a function to print table of a given number
def table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
        
table(34)

def table(*n):
    for j in n:
        for i in range(1, 11):
            print(f"{j} x {i} = {j*i}")


# table(12, 2, 9, 5)
table(2, 27)


# l1 = [10, 20, 30, 40, 50]

# for i in l1:
#     print(i)
