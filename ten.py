# compute_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def power(base, exp):
    return base ** exp

# main.py
import compute_utils

print("Addition:", compute_utils.add(5, 3))
print("Subtraction:", compute_utils.subtract(10, 4))
print("Multiplication:", compute_utils.multiply(6, 7))
print("Division:", compute_utils.divide(15, 3))
print("Factorial:", compute_utils.factorial(5))
print("Power:", compute_utils.power(2, 3))
