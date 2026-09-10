# Q Is enterd number is a prime numebr ?

def is_prime(num):
    for i in range(2,int(num * 0.5) +1):
        if num%i==0:
            return "not prime"
    return "prime"
num = int(input("Enter the number: "))

print(is_prime(num))