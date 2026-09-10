# Q create a function to add two numbers and store result in 'result' variable.
# create a another function which double value of 'result'

# Global variable that is outside of any function
#local variable that is inside a function


def add(a,b):
    result = a + b 
    return result

print(add(7,9))

global result
def double(num):
    return num*2

print(double(add(7,9)))
# concept 1
# scope of variable
# 1. global variable
# 2. local variable

# name = "radha"  # global variable


# def greet():
#     value = "100"  # local variable


# print(name)
# print(value)


# concept 2
# 1. global
