def fact(i):
    if i == 0:
        return 1
    else:
        return i * fact(i - 1)
i=int(input("Enter a number: "))
if i<0:
    print("Please enter a positive number")
else:
    print("The factorial of",i,"is",fact(i))