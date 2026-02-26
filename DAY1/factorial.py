def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")