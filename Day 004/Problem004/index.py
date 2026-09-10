# Q4. why "Type of class " include "__main__" ?


class Person:
    pass


obj = Person()

print(type(obj))


import jd

obj = jd.Students()  # object has been created
obj.info()  # calling function info

print(type(obj))

# # 
# class Person:
#     pass


# obj1 = Person()
# print(type(obj1))
