#Create a Customer class with private attributes for name, address, and phone_number. Implement methods for get_name(), get_address(), and get_phone_number() with appropriate data validation.

class Customer:
    def __init__(self, name, address, phone_number):
        """Initialize the customer with name, address, and phone number."""
        self.__set_name(name)
        self.__set_address(address)
        self.__set_phone_number(phone_number)

    def __set_name(self, name):
        """Set the customer's name with validation."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = name.strip()

    def __set_address(self, address):
        """Set the customer's address with validation."""
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Address must be a non-empty string.")
        self.__address = address.strip()

    def __set_phone_number(self, phone_number):
        """Set the customer's phone number with validation."""
        if not isinstance(phone_number, str) or not phone_number.strip():
            raise ValueError("Phone number must be a non-empty string.")
        if not phone_number.isdigit() or len(phone_number) < 10:
            raise ValueError("Phone number must be a valid numeric string with at least 10 digits.")
        self.__phone_number = phone_number.strip()

    def get_name(self):
        """Return the customer's name."""
        return self.__name

    def get_address(self):
        """Return the customer's address."""
        return self.__address

    def get_phone_number(self):
        """Return the customer's phone number."""
        return self.__phone_number

# Example usage:
if __name__ == "__main__":
    try:
        customer = Customer("John Doe", "123 Main St", "1234567890")
        print("Name:", customer.get_name())         
        print("Address:", customer.get_address())    
        print("Phone Number:", customer.get_phone_number())  

       
       
    except ValueError as e:
        print("Error:", e)