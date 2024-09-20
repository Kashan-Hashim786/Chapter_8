def greatestNumber(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the greatest number")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the greatest number")
    else:
        print(f"{num3} is the greatest number")

greatestNumber(3,2,1)
greatestNumber(56,76,33)
greatestNumber(23,34,45)
