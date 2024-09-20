def patterns(n):
    if n <= 0:
        print("The number must be greater then 0")
    else:
        print("*" * (n))
        patterns(n-1)

patterns(0)