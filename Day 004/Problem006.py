# Q how to create a constructor ?


# class Students:

#     def __init__(self):
#         self.name = "jp"
#         self.age = 21
#         self.location = "Ajmer"
#         print("calling from constructor")


# obj1 = Students()
# # obj1 = Students()




# print(obj1.name)


# shortuct = ctrl + shift + enter (create a line above)
class Students:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        print("calling from constructor")

    def info(self):
        print("adfjakdf")


obj1 = Students("ram", 21, "india")
obj1.info()
# obj1 = Students()

# print(obj1.name)

# 1.self = varaible or function will denote class
# 2.self.name(parameter) = name(argument)
# 3.self = we can write anything in this
