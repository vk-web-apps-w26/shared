#!/usr/bin/env python3
"""
Simple calculator that takes two numbers as input and outputs their sum.
"""

def main():
    # Get first number from user
    num1 = float(input("Enter the first number: "))
    
    # Get second number from user
    num2 = float(input("Enter the second number: "))
    
    # Calculate sum
    result = num1 + num2
    
    # Display result
    print(f"\nThe sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()