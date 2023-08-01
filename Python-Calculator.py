Development

# Python-Calculator
Create a basic calculator in Python.

def add(num1, num2):
    return num1 + num2
    
def subtract(num1, num2):
    return num1 - num2
    
def multiply(num1, num2):
    return num1 * nym 2
    
def divide(num1, num2):
    return num1 / num2
    
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
        
select = int(input("Select a opetion from 1, 2, 3, 4: "))

num_1 = int(input("Enter first value: "))
num_2 = int(input("Enter second value: "))

if select == 1
    print(num1, " + ", num_2, " = ", add(num_1, num_2))
else if select == 2
    print(num1, " - ", num_2, " = ", subtract(num_1, num_2))
else if select == 3
    print(num1, " x ", num_2, " = ", multiply(num_1, num_2))
else if select == 4
    print(num1, " / ", num_2, " = ", divide(num_1, num_2))
else
    print("ïnvalid input")