def add(x,y):
    return(x + y)

def subtract(x,y):
    return(x - y)

def multiply(x,y):
    return(x * y)

def divide(x,y):
    return(x / y)

print("Make your choice: ")
print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))
    print("Thank You! ")
elif choice == '2':
    print(num1, "-", num2, "=",subtract(num1, num2))
    print("Thank You! ")
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))
    print("Thank You! ")
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))
    print("Thank You! ")
else:
    print("Invalid choice")
    print("Thank You! ")