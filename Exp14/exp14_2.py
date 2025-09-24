class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount
        print(f"Discount of {discount_percent}% applied. New Price: ₹{self.price:.2f}")


# (a) Create two book objects
book1 = Book("The Alchemist", "Paulo Coelho", 499)
book2 = Book("Python Programming", "John Zelle", 799)

print("📚 Book Details:")
book1.display_details()
book2.display_details()

# (b) Apply 10% discount to book2
print("🎯 Applying 10% discount on 'Python Programming':")
book2.apply_discount(10)
book2.display_details()
