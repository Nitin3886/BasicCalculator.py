# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2

def calculator():
    print("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n" \
            "5. Exit\n")

    while True:
        try:
            select = int(input("Select operations from 1, 2, 3, 4, or 5 to exit: "))
            if select == 5:
                print("Exiting...")
                break

            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if select == 1:
                print(number_1, "+", number_2, "=", add(number_1, number_2))
            elif select == 2:
                print(number_1, "-", number_2, "=", subtract(number_1, number_2))
            elif select == 3:
                print(number_1, "*", number_2, "=", multiply(number_1, number_2))
            elif select == 4:
                result = divide(number_1, number_2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(number_1, "/", number_2, "=", result)
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    calculator()
