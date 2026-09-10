# Q1. what is a class ?

# 1. variables (attributes)
# 2. methods (function)

# myth  => class consist of variable or methods (this will always not true)
# class is a blue print for creating object.

# concept 1

# 1. variable = small letters
# 2. class = first word must be capital


class Students:
    name = "jai prakash"

    def info(self):
        print("calling from Students class")


obj = Students()
obj.age = 21
obj.work = "Engineer"
# print(obj.__dict__)
print(obj.age)
obj.info()
print(obj.name)
print(obj.work)


# concept 2 (accessing methods and variables)
# 1. method = method_name()
# 2. variables = .variable_name


# 1. shortcut
# 1. ctrl + shift + z = redo
