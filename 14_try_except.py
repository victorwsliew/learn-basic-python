try:
    value = 10/0
    number =  int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid Input")

