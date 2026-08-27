import json
import tkinter as tk
from tkinter import ttk, messagebox
class Product:
    def __init__(self, product_id, name, category, unit_price, quantity, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.quantity = quantity
        self.supplier = supplier

    def display(self):
        print(
            f"ID: {self.product_id:<5} "
            f"Name: {self.name:<15} "
            f"Category: {self.category:<15} "
            f"unit_price: {self.unit_price:<10} "
            f"Quantity: {self.quantity:<5} "
            f"Supplier: {self.supplier}"
        )


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for p in self.products:
            if p.product_id == product.product_id:
                return False

        self.products.append(product)
        return True
manager = ProductManager()
#saving data
   
def add_product():
    product_id = int(product_id_entry.get())
    name = name_entry.get()
    category = category_entry.get()
    unit_price = float(unit_price_entry.get())
    quantity = int(quantity_entry.get())
    supplier = supplier_entry.get()

    product = Product(
        product_id,
        name,
        category,
        unit_price,
        quantity,
        supplier
    )

    if manager.add_product(product):
        messagebox.showinfo("Success", "Product added successfully!")
        display_products()
        product_id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        unit_price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        supplier_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Error", "Product ID already exists.")
        
def save_products(self):
        data  = []
        for product in self.products:
            data.append({
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "unit_price": product.unit_price,
                "quantity":product.quantity,
                "supplier": product.supplier

            })
        with open("products.json", "w") as file:
                json.dump(data, file, indent=4, sort_keys = True)
        print("Products saved successfully.")
def display_products():
    for item in product_table.get_children():
        product_table.delete(item)

    for product in manager.products:
        product_table.insert(
            "",
            tk.END,
            values=(
                product.product_id,
                product.name,
                product.category,
                product.unit_price,
                product.quantity,
                product.supplier
            )
        )
def update_product():
    try:
        product_id = int(product_id_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Product ID.")
        return

    for product in manager.products:

        if product.product_id == product_id:

            product.name = name_entry.get()
            product.category = category_entry.get()
            product.unit_price = float(unit_price_entry.get())
            product.quantity = int(quantity_entry.get())
            product.supplier = supplier_entry.get()

            display_products()

            messagebox.showinfo(
                "Success",
                "Product updated successfully!"
            )

            return

    messagebox.showerror("Error", "Product not found.")
root = tk.Tk()
root.title("Supermarket inventory Management system")
root.geometry("900x600")


product_id_label = ttk.Label(root, text="Product ID:")
product_id_label.grid(row=0, column=0, padx=10, pady=10)

product_id_entry = ttk.Entry(root)
product_id_entry.grid(row=0, column=1, padx=10, pady=10)

name_label= ttk.Label(root, text="Product Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)

name_entry = ttk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

category_label= ttk.Label(root, text="Category:")
category_label.grid(row=2, column=0, padx=10, pady=10)

category_entry = ttk.Entry(root)
category_entry.grid(row=2, column=1, padx=10, pady=10)

unit_price_label= ttk.Label(root, text="Unit Price:")
unit_price_label.grid(row=3, column=0, padx=10, pady=10)

unit_price_entry = ttk.Entry(root)
unit_price_entry.grid(row=3, column=1, padx=10, pady=10)

quantity_label= ttk.Label(root, text="Quantity:")
quantity_label.grid(row=4, column=0, padx=10, pady=10)

quantity_entry = ttk.Entry(root)
quantity_entry.grid(row=4, column=1, padx=10, pady=10)


supplier_label= ttk.Label(root, text="Supplier:")
supplier_label.grid(row=5, column=0, padx=10, pady=10)

supplier_entry = ttk.Entry(root)
supplier_entry.grid(row=5, column=1, padx=10, pady=10)

add_button = ttk.Button(root, text="Add Product", command=add_product)

update_button = ttk.Button(
    root,
    text="Update Product",
    command=update_product
)

update_button.grid(row=6, column=1, padx=10, pady=20)

add_button.grid(row=6, column=0, padx=10, pady=20)
columns = ("ID", "Name", "Category", "Price", "Quantity", "Supplier")

product_table = ttk.Treeview(root, columns=columns, show="headings")
product_table.heading("ID", text="Product ID")
product_table.heading("Name", text="Name")
product_table.heading("Category", text="Category")
product_table.heading("Price", text="Unit Price")
product_table.heading("Quantity", text="Quantity")
product_table.heading("Supplier", text="Supplier")

product_table.column("ID", width=80)
product_table.column("Name", width=150)
product_table.column("Category", width=120)
product_table.column("Price", width=100)
product_table.column("Quantity", width=100)
product_table.column("Supplier", width=150)

product_table.grid(
    row=8,
    column=0,
    columnspan=4,
    padx=10,
    pady=20
)


root.mainloop()










def load_product(self):
        try:
           with open("products.json", "r") as file:
               data = json.load(file)
               for item in data:
                   product = Product(
                       item["product_id"],
                    item["name"],
                    item["category"],
                    item["unit_price"],
                    item["quantity"],
                    item["supplier"]  
                   )
                   self.products.append(product)
        except FileNotFoundError:
            self.product = []
    # ADD PRODUCT
def add_product(self):
        print("\n===== ADD PRODUCT =====")

        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        category = input("Enter category: ")
        unit_price = float(input("Enter Unit_price: "))
        quantity = int(input("Enter quantity: kg"))
        supplier = input("Enter supplier: ")

        # Check duplicate ID
        for product in self.products:
            if product.product_id == product_id:
                print("Product ID already exists.")
                return

        product = Product(
            product_id,
            name,
            category,
            unit_price,
            quantity,
            supplier
        )

        self.products.append(product)

        print("Product added successfully.")

        self.products.append(product)

        self.save_products()

        print("Product added successfully.")
    # DELETE PRODUCT
def delete_product(self):
        print("\n===== DELETE PRODUCT =====")

        product_id = int(input("Enter product ID to delete: "))

        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                self.save_products()

                    
                print("Product deleted successfully.")
                return

        print("Product not found.")

    # UPDATE PRODUCT
def update_product(self):
        print("\n===== UPDATE PRODUCT =====")

        product_id = int(input("Enter product ID to update: "))

        for product in self.products:
            if product.product_id == product_id:

                print("\nLeave the field empty if you don't want to change it.")

                name = input(f"Name ({product.name}): ")
                category = input(f"Category ({product.category}): ")
                unit_price = input(f"Unit_price ({product.unit_price}): ")
                quantity = input(f"Quantity ({product.quantity}): ")
                supplier = input(f"Supplier ({product.supplier}): ")

                if name != "":
                    product.name = name

                if category != "":
                    product.category = category

                if unit_price != "":
                    product.unit_price = float(unit_price)

                if quantity != "":
                    product.quantity = int(quantity)

                if supplier != "":
                    product.supplier = supplier
                self.save_products()


                print("Product updated successfully.")
                return

        print("Product not found.")
    

    # SEARCH PRODUCT
def search_product(self):
        print("\n===== SEARCH PRODUCT =====")

        keyword = input("Enter product name, category, supplier, or ID: ")

        found = False

        for product in self.products:

            if (
                keyword.lower() in product.name.lower()
                or keyword.lower() in product.category.lower()
                or keyword.lower() in product.supplier.lower()
                or keyword == str(product.product_id)
            ):
                product.display()
                found = True

        if not found:
            print("No product found.")

    # DISPLAY PRODUCTS
def display_products(self):
        print("\n===== ALL PRODUCTS =====")

        if len(self.products) == 0:
            print("No products available.")
            return

        for product in self.products:
            product.display()


# ==================================================
# MAIN PROGRAM
# ==================================================

manager = ProductManager()
manager.load_product()
while True:


    print("\n")
    print("========================================")
    print("       SUPERMARKET PRODUCT SYSTEM")
    print("========================================")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Display All Products")
    print("6. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_product()

    elif choice == "2":
        manager.search_product()

    elif choice == "3":
        manager.update_product()

    elif choice == "4":
        manager.delete_product()

    elif choice == "5":
        manager.display_products()

    elif choice == "6":
        print("Thank you for using the supermarket system.")
        break

    else:
        print("Invalid choice. Please enter 1-6.")

    
