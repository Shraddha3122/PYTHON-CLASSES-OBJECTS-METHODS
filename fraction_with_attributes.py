# Develop a class Fraction with attributes for numerator and denominator.
# Add methods for arithmetic operations and reducing fractions.

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()  # Reduce the fraction upon initialization

    def reduce(self):
        """Reduce the fraction to its simplest form."""
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

        # Ensure the denominator is positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

# Example usage:
if __name__ == "__main__":
    frac1 = Fraction(1, 2)
    frac2 = Fraction(3, 4)

    print(f"Fraction 1: {frac1}")  
    print(f"Fraction 2: {frac2}")  

    # Addition
    result_add = frac1 + frac2
    print(f"Addition: {result_add}") 

    # Subtraction
    result_sub = frac1 - frac2
    print(f"Subtraction: {result_sub}") 

    # Multiplication
    result_mul = frac1 * frac2
    print(f"Multiplication: {result_mul}")  

    # Division
    result_div = frac1 / frac2
    print(f"Division: {result_div}")  