def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  n + sum(n - 1)


print("The sum of number is ",sum(10))
print("The sum of number is ",sum(20))
print("The sum of number is ",sum(30))