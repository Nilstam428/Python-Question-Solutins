# Q can a single condition have multiple return exist in a function ?  # answer = no


def greet():
    # return "hello world"
    return "good morning"


print(greet())


def number(n):
    if n % 2 == 0:
        return "even"
        return "dfnkj"
    else:
        return "odd"
        return "dfnkj"

print(number(31))