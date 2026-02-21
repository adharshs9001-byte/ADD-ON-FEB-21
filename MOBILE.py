class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_amount):
        if discount_amount > 0 and discount_amount < self.price:
            self.price -= discount_amount
            print(f"Discount of {discount_amount} applied. New price: {self.price}")
        else:
            print("Invalid discount amount.")

    def display_mobile(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")


# Example usage
mobile1 = Mobile("Samsung", "Galaxy S25", 80000)

mobile1.display_mobile()
mobile1.apply_discount(5000)
mobile1.display_mobile()