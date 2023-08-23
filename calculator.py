def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice :
            case '1':
                print(num1, "+", num2, "=", add(num1, num2))

            case '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            case '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            case '4':
                print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Choose 1, 2, 3 or 4")
        continue

    next_calculation = input("Wanna do another calculation? (yes/no): ")

    if next_calculation == "no":
        break

    else:
        continue
