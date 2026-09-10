# how to know that element in list start with given charchter

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
char = "e"
result = [element for element in my_list if element.startswith(char)]
print(result)