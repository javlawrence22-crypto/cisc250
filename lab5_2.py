# Name: Javrick Lawrence
# LAB 5-2
# Date: 2026-5-28
# ============================================================

# Task 1.1
class Product:
    """Represents a physical product in the inventory system."""

    # Task 1.2
    def __init__(self, name, price, stock=0):
        """Initializes a Product object with name, price, and stock."""
        self.name = name
        self.price = price
        self.stock = stock

    # Task 1.3
    def display_details(self):
        """Displays the details of the product."""
        print("\nProduct Details")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

    # Task 1.4
    def update_stock(self, quantity):
        """Safely increases or decreases the stock quantity."""

        if self.stock + quantity < 0:
            print(f"Cannot update stock by {quantity}. Stock cannot go below zero.")
        else:
            self.stock += quantity
            print(f"Stock updated by {quantity}. New stock: {self.stock}")


# Task 2.1
class DigitalProduct(Product):
    """Represents a downloadable digital product."""

    # Task 2.2
    def __init__(self, name, price, download_link):
        """Initializes a DigitalProduct object."""
        super().__init__(name, price, 9999)
        self.download_link = download_link

    # Task 2.3
    def display_details(self):
        """Displays the details of the digital product."""
        print("Digital Product Details")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Download Link: {self.download_link}")


# =============================================================================
# Task 3: Instantiate and Test Objects
# =============================================================================

# Task 3.1 - Create one Product and one DigitalProduct object
product1 = Product("Wireless Mouse", 29.99, 10)

digital_product1 = DigitalProduct(
    " INFO TECHNOLOGY GUIDE EBOOK",
    14.99,
    "https://download.example.com/INFO_TECHNOLOGY_GUIDE_EBOOK"
)
# Task 3.2 - Positive stock update
print("\nUpdating stock by +4")
product1.update_stock(4)

# Task 3.3 - Display details after update
product1.display_details()

# Task 3.2 - Negative stock update that remains above zero
print("\nUpdating stock by -8")
product1.update_stock(-8)

# Task 3.3 - Display details after update
product1.display_details()

# Task 3.2 - Negative stock update that would go below zero
print("\nUpdating stock by -20")
product1.update_stock(-20)

# Task 3.3 - Display details after update attempt
product1.display_details()

# Task 3.4 - Display DigitalProduct details
print("\nDigital Product Details:")
digital_product1.display_details()