# Write a base class Media and extend it into Book, DVD, and Magazine. 
# Include a common method display_info and unique methods for each subclass.


class Media:
    def __init__(self, title, publisher, year):
        self.title = title
        self.publisher = publisher
        self.year = year

    def display_info(self):
        return f"Title: {self.title}, Publisher: {self.publisher}, Year: {self.year}"


class Book(Media):
    def __init__(self, title, author, publisher, year, pages):
        super().__init__(title, publisher, year)
        self.author = author
        self.pages = pages

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Author: {self.author}, Pages: {self.pages}"

    def read(self):
        return f"You are reading '{self.title}' by {self.author}."


class DVD(Media):
    def __init__(self, title, director, publisher, year, duration):
        super().__init__(title, publisher, year)
        self.director = director
        self.duration = duration

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Director: {self.director}, Duration: {self.duration} minutes"

    def watch(self):
        return f"You are watching '{self.title}' directed by {self.director}."


class Magazine(Media):
    def __init__(self, title, publisher, year, issue_number):
        super().__init__(title, publisher, year)
        self.issue_number = issue_number

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Issue Number: {self.issue_number}"

    def browse(self):
        return f"You are browsing through '{self.title}', Issue Number: {self.issue_number}."


# Example usage:
if __name__ == "__main__":
    book = Book("1984", "George Orwell", "Secker & Warburg", 1949, 328)
    dvd = DVD("Inception", "Christopher Nolan", "Warner Bros.", 2010, 148)
    magazine = Magazine("National Geographic", "National Geographic Society", 2023, 5)

    print(book.display_info())
    print(book.read())

    print(dvd.display_info())
    print(dvd.watch())

    print(magazine.display_info())
    print(magazine.browse())