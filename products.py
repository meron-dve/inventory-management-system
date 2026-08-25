class Product:
    def __init__(self, product_id, name, category ,price , quantity ):
           self.product_id = product_id
           self.name = name
           self.category = category
           self.price = price
           self.quantity = quantity
    def display(self):
        print(f"{self.product_id} - {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price} ETB")
        print(f"Stock: {self.quantity}")

milk = Product("P001", "Milk", "Dairy", 100, 30)
rice = Product("P002", "Rice", "Food", 800, 50)
bread = Product("P003", "Bread", "Bakery", 60, 40)
print(milk.display())