def fib_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using simple recursion.
    fib_recursive(0) == 0
    fib_recursive(1) == 1
    Note: exponential time for large n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def get_user_input():
    """
    Prompt user for:
      - n: index of Fibonacci number (non-negative integer)
      - comment: a short comment string to include as generated comment
    Returns: (n:int, comment:str)
    """
    while True:
        try:
            n = int(input("Enter n (non-negative integer) for Fibonacci: ").strip())
            if n >= 0:
                break
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Please enter a valid integer.")

    comment = input("Enter a short comment to generate (optional): ").strip()
    return n, comment

def main():
    n, comment = get_user_input()

    # Generated comment (from user)
    if comment:
        print(f"# {comment}")

    try:
        result = fib_recursive(n)
        print(f"Fibonacci number F({n}) = {result}")
    except RecursionError:
        print("Error: recursion depth exceeded for the chosen n. Try a smaller n.")

if __name__ == "__main__":
    main()