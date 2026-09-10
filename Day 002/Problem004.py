# Q write a function to check (number is prime or not)

def checkPrime(number: int):
    if number < 2:
        print("number is not a prime number")
    elif number == 2:
        print("2 is a prime number")
    elif number > 2:
        divisors = []
        for i in range(2, int(number*0.5)+1):
            if number % i == 0:
                divisors.append(i)
        if len(divisors)>0:
            print(f"{number} is not a prime number because it isdivisible by {', '.join(map(str, divisors))}")        
        else:
            print(f"{number} is a prime number")
            #     print(f"{number} is not a prime number because it is divided by { i }")
            #     break        
            # else:
            #     print(f"{number} is a prime number")
    else:
        print("invalid input")


checkPrime(int(input("Enter a number: ")))


# while True:
#     for i in range(1, 10):
#         if i == 8:
#             print("out of loop")
#     break
