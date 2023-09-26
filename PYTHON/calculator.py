def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print( "Cannot divide by zero")

print("Select operation you want to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice\n 1\n2\n3\n4\n:-  ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print(a, "+", b, "=", add(a, b))
elif choice == '2':
    print(a, "-", b, "=", subtract(a, b))
elif choice == '3':
    print(a, "*", b, "=", multiply(a, b))
elif choice == '4':
    print(a, "/", b, "=", divide(a, b))
else:
    print("Invalid input")
