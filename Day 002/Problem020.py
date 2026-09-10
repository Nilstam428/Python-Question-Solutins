# Q how to access values in dictionary
dict1 = {'name': 'nilesh', 'age': 24, 'location': 'chittorgarh'}

# can use [] also but give none when key not present in the dict
print(dict1['location'])
print(dict1['age'])

# .get() method more better error handling
print(dict1.get('education', 'btech'))
print(dict1.get('name'))

# can also use .item() to get collecion of key and value 
for keys, values in dict1.items():
    print(f"{keys}: {values}", end=", ")

# dictionary does not have indexing so i want to get specifically 3rd element then either we can convert this to list
# 2nd way is using enumerate function.
