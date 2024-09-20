





n = int(input("Enter any number : "))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
       return  n * factorial(n - 1)

print(f"The factorial of {n} is {factorial(n)}")