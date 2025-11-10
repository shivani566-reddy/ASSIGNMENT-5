def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_user_input() -> Tuple[float, float, str]:
    while True:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ").strip()
            if operation in ('+', '-', '*', '/'):
                return x, y, operation
            else:
                print("Invalid operation. Please enter one of +, -, *, /.")
        except ValueError:
            print("Please enter valid numbers.")

def main():
    print("Simple Calculator")
    while True:
        x, y, operation = get_user_input()
        if operation == '+':
            result = add(x, y)
        elif operation == '-':
            result = subtract(x, y)
        elif operation == '*':
            result = multiply(x, y)
        elif operation == '/':
            try:
                result = divide(x, y)
            except ValueError as e:
                print(e)
                continue
        
        print(f"The result of {x} {operation} {y} = {result}")
        if input("Do you want to perform another calculation? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()