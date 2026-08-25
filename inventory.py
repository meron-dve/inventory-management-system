class inventory:
    def __init__(self):
        self.products = [] 
    def add_product(self, product):
        self.products.append(product)
        print("product added sucessfully.")
    def view_products(self):
        if len(self.products) == 0:
            print("inventory is empty.")
            return
        for product in self.products:
            product.display()
    def search_product(self, name):
        for product in self.products:
            if product.name.lower() ==name.lower():
                return product  
        print("product not found.")
        return None
    def sell_product(self, product_id,quantity):  
        for product in self.products:  
            if product.product_id == product_id:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print("product sold succesfully.")
                else:
                     print("not enough stock available")
                return 
        print("product not found")
    def low_stock(self,limit=5):
      print("\nlow-stock products.")
      found = False
      for product in self.products:
        if product.quantity <= limit:
           print(product.name,"-",product.quantity,"left")
           found = True
      if not found:
        print("No products are low in stock.")
    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price *product.quantity
        return total
    def view_by_category(self,category):
        found = False 
        for product in self.products:
            if product.category.lower() == category.lower():
                product.display()
                found = True 
        if not found: 
            print("No products found in this category")   
my_inventory =inventory()   
my_inventory.view_products()         


      
                   
                

        