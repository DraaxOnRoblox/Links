# INSTRUCTIONS HOW TO USE : 

# INSTALL PYTHON (https://python.org)
# INSTALL PYCHARM COMMUNITY (https://jetbrains.com/pycharm/)

# HOW TO CREATE A SIMPLE CALCULATOR WITH PYTHON (by DraaxOnRoblox#0001)

print("Select an operation to perform : ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter your first number : ")
    num2 = input("Enter your second number : ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter your first number : ")
    num2 = input("Enter your second number : ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter your first number : ")
    num2 = input("Enter your second number : ")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter your first number : ")
    num2 = input("Enter your second number : ")
    print("The result is " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")
