def check_number(n):
    if n > 0:
        print("the nmuber is positive")
    elif n < 0:
        print("The number is negative")
    else:
        print("The number is zero")

        number=int(input("Enter a number:"))
        check_number(number)