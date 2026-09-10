# Q7. what are the three properties of object ?


# 1. object can have variables
# 2. object can have methods
# 3. two object have different unique id


# id = (variable , function , class) provides unique value

# myth = id does not denotes memory address
# name = "radha"
# print(id(name))

# name = "ram"
# print(id(name))

# 👇 id will be same here
x = 10
print(id(x))

y = x
print(id(y))


class Students:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        # print("calling from constructor")

    def info(self):
        print("adfjakdf")


# two object will always have different id

obj1 = Students("jp", 21, "Ajmer")
obj2 = Students("jp", 21, "Ajmer")


print(id(obj1))
print(id(obj2))
