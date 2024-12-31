# Create a Calculator class with overloaded methods for add(). 
#The add() method should be able to handle different combinations of integer, float, and string arguments.

class Calculator:
    def add(self, *args):
        """Add multiple numbers (int, float) or strings that can be converted to numbers."""
        total = 0
        for arg in args:
            if isinstance(arg, (int, float)):
                total += arg
            elif isinstance(arg, str):
                try:
                    # Attempt to convert the string to a float
                    total += float(arg)
                except ValueError:
                    raise ValueError(f"Cannot convert '{arg}' to a number.")
            else:
                raise TypeError(f"Unsupported type: {type(arg)}. Only int, float, or str are allowed.")
        return total

# Example usage:
if __name__ == "__main__":
    calculator = Calculator()
    
    # Adding integers
    print(calculator.add(1, 2, 3))  
    
    # Adding floats
    print(calculator.add(1.5, 2.5, 3.0))  
    
    # Adding a mix of integers and floats
    print(calculator.add(1, 2.5, 3)) 
    
    # Adding strings that can be converted to numbers
    print(calculator.add("1", "2.5", "3"))  
    
    # Adding a mix of numbers and strings
    print(calculator.add(1, "2", 3.5))  
    
   