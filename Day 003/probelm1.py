# 1. name = "yourName"
# 2. function => "python"
# 3. function => odd / even
# 4. function => table print
# Table printing


name="Nilesh Tamboli"

# get table
def get_table(num):
  # num = int(input("Enter a number"))
  count = 1
  while count <= 10:
     print(f"{num}x{count}={num*count}")
     count+=1
  # for i in range(1,11):
  #   print(f"{num}x{i}={num*i}")

# python 
def python():
  print("Hello Python")

  
# Even odd
def even_odd(n: int) -> int:
  n = int(input("Enter a number"))
  if(n%2==0):
        print(f"{n} is even !!")
  else:
        print(f"{n} odd number!!")

# num = int(input("Enter a number: "))
# print(even_odd())
