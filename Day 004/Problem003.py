# can we assign variable to empty class ?
# it is possible


class Students:
    pass


obj = Students()
obj.Name = "sandeep"  # dynamically
obj.age = 20
print(obj.__dict__)

print(obj.Name)
print(obj.age)


print(obj.__dict__)


# concept 1

# class = empty (we can assign only varibles )

# concept 2

# at run time dictionary will be created
