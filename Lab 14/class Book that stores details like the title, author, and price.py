
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    def apply_discount(self, discount_percent):
        self.price = self.price - (self.price * discount_percent / 100)
book1 = Book("yedu chapala katha", "RGV", 500)
book2 = Book("IMMORTALS", "Sandeep reddy", 650)
print("Book 1 Details:")
book1.display_details()
print("\nBook 2 Details:")
book2.display_details()
book2.apply_discount(10)
print("\nAfter 10% Discount on Book 2:")
book2.display_details()
