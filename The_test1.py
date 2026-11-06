def add(a,b):
    return a + b
def subract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

try:
    print("1 add")
    print("2 subbract")
    print("3 multiply")
    print("4 division")

    choice = input("Choise operation (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice =="1":
        print("Result:", add(a, b))
    elif choice =="2":
        print("Result:", subract(a, b))
    elif choice =="3":
        print("Result:", multiply(a, b))
    if choice =="4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choise!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")