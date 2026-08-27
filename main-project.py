import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

FILE_NAME = "products.json"


# ==================================================
# DATA CLASSES (same logic as before)
# ==================================================

class Product:
    def __init__(self, product_id, name, category, unit_price, quantity, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.quantity = quantity
        self.supplier = supplier

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "unit_price": self.unit_price,
            "quantity": self.quantity,
            "supplier": self.supplier,
        }

    @staticmethod
    def from_dict(data):
        return Product(
            data["product_id"],
            data["name"],
            data["category"],
            data["unit_price"],
            data["quantity"],
            data["supplier"],
        )


class ProductManager:
    def __init__(self):
        self.products = []
        self.load_from_file()

    def save_to_file(self):
        data = [p.to_dict() for p in self.products]
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        if not os.path.exists(FILE_NAME):
            return
        try:
            with open(FILE_NAME, "r") as f:
                data = json.load(f)
                self.products = [Product.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            self.products = []

    def find_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    # ---- Core actions now RETURN results instead of using input()/print() ----

    def add_product(self, product_id, name, category, unit_price, quantity, supplier):
        if self.find_by_id(product_id):
            return False, "Product ID already exists."

        product = Product(product_id, name, category, unit_price, quantity, supplier)
        self.products.append(product)
        self.save_to_file()
        return True, "Product added successfully."

    def delete_product(self, product_id):
        product = self.find_by_id(product_id)
        if not product:
            return False, "Product not found."

        self.products.remove(product)
        self.save_to_file()
        return True, "Product deleted successfully."

    def update_product(self, product_id, name, category, unit_price, quantity, supplier):
        product = self.find_by_id(product_id)
        if not product:
            return False, "Product not found."

        # Only update fields that were actually filled in
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

        self.save_to_file()
        return True, "Product updated successfully."

    def search_products(self, keyword):
        keyword = keyword.lower()
        results = [
            p for p in self.products
            if keyword in p.name.lower()
            or keyword in p.category.lower()
            or keyword in p.supplier.lower()
            or keyword == str(p.product_id)
        ]
        return results


# ==================================================
# GUI APPLICATION
# ==================================================

class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.manager = ProductManager()

        self.root.title("Supermarket Product System")
        self.root.geometry("900x550")

        self.selected_id = None  # tracks which row is selected in the table

        self.build_form()
        self.build_buttons()
        self.build_table()
        self.refresh_table()

    # ---------- FORM (input fields) ----------
    def build_form(self):
        form_frame = tk.LabelFrame(self.root, text="Product Details", padx=10, pady=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        labels = ["Product ID", "Name", "Category", "Unit Price", "Quantity", "Supplier"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label + ":").grid(row=0, column=i * 2, padx=5, pady=5, sticky="w")
            entry = tk.Entry(form_frame, width=12)
            entry.grid(row=0, column=i * 2 + 1, padx=5, pady=5)
            self.entries[label] = entry

    # ---------- BUTTONS ----------
    def build_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(button_frame, text="Add", width=12, command=self.on_add).pack(side="left", padx=5)
        tk.Button(button_frame, text="Update", width=12, command=self.on_update).pack(side="left", padx=5)
        tk.Button(button_frame, text="Delete", width=12, command=self.on_delete).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear Form", width=12, command=self.clear_form).pack(side="left", padx=5)

        # Search box
        tk.Label(button_frame, text="   Search:").pack(side="left", padx=(20, 5))
        self.search_entry = tk.Entry(button_frame, width=20)
        self.search_entry.pack(side="left", padx=5)
        tk.Button(button_frame, text="Search", width=10, command=self.on_search).pack(side="left", padx=5)
        tk.Button(button_frame, text="Show All", width=10, command=self.refresh_table).pack(side="left", padx=5)

    # ---------- TABLE (Treeview) ----------
    def build_table(self):
        columns = ("ID", "Name", "Category", "Unit Price", "Quantity", "Supplier")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # When a row is clicked, load its values into the form (useful for update/delete)
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    # ---------- TABLE HELPERS ----------
    def refresh_table(self, products=None):
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        products = products if products is not None else self.manager.products

        for p in products:
            self.tree.insert("", "end", values=(
                p.product_id, p.name, p.category, p.unit_price, p.quantity, p.supplier
            ))

    def on_row_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")

        self.clear_form()
        self.entries["Product ID"].insert(0, values[0])
        self.entries["Name"].insert(0, values[1])
        self.entries["Category"].insert(0, values[2])
        self.entries["Unit Price"].insert(0, values[3])
        self.entries["Quantity"].insert(0, values[4])
        self.entries["Supplier"].insert(0, values[5])

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    # ---------- BUTTON ACTIONS ----------
    def get_form_values(self):
        return {
            "id": self.entries["Product ID"].get().strip(),
            "name": self.entries["Name"].get().strip(),
            "category": self.entries["Category"].get().strip(),
            "unit_price": self.entries["Unit Price"].get().strip(),
            "quantity": self.entries["Quantity"].get().strip(),
            "supplier": self.entries["Supplier"].get().strip(),
        }

    def on_add(self):
        values = self.get_form_values()

        if not values["id"] or not values["name"]:
            messagebox.showerror("Error", "Product ID and Name are required.")
            return

        try:
            product_id = int(values["id"])
            unit_price = float(values["unit_price"]) if values["unit_price"] else 0.0
            quantity = int(values["quantity"]) if values["quantity"] else 0
        except ValueError:
            messagebox.showerror("Error", "ID must be a number, Price must be a number, Quantity must be a number.")
            return

        success, message = self.manager.add_product(
            product_id, values["name"], values["category"], unit_price, quantity, values["supplier"]
        )

        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
            self.refresh_table()
        else:
            messagebox.showerror("Error", message)

    def on_update(self):
        values = self.get_form_values()

        if not values["id"]:
            messagebox.showerror("Error", "Enter the Product ID of the item to update.")
            return

        try:
            product_id = int(values["id"])
        except ValueError:
            messagebox.showerror("Error", "Product ID must be a number.")
            return

        success, message = self.manager.update_product(
            product_id, values["name"], values["category"],
            values["unit_price"], values["quantity"], values["supplier"]
        )

        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
            self.refresh_table()
        else:
            messagebox.showerror("Error", message)

    def on_delete(self):
        values = self.get_form_values()

        if not values["id"]:
            messagebox.showerror("Error", "Enter the Product ID of the item to delete.")
            return

        try:
            product_id = int(values["id"])
        except ValueError:
            messagebox.showerror("Error", "Product ID must be a number.")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Delete product ID {product_id}?")
        if not confirm:
            return

        success, message = self.manager.delete_product(product_id)

        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
            self.refresh_table()
        else:
            messagebox.showerror("Error", message)

    def on_search(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            self.refresh_table()
            return

        results = self.manager.search_products(keyword)

        if not results:
            messagebox.showinfo("Search", "No product found.")

        self.refresh_table(results)


# ==================================================
# RUN APP
# ==================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketApp(root)
    root.mainloop()