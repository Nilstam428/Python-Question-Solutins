# Q8. how many types of variables are there in python class ?

# there are two types of variables

# 1. instance variable (dynamic variable)= variable which inside a constructor are instance variables
# 2. class variable (static variable) = variable which outside of a constructor


class Students:
    x = 10 # static variable
    y = 20
    lang = "python"

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        # name , age , location (instance variable)
        print("calling from constructor")

    def info(self):
        print("adfjakdf")
