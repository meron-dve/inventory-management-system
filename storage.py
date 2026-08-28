import json
from products import Product
def save_products(products):
    data = []

    for product in products:
        data.append({
            "product_id": product.product_id,
            "name" : product.name,
            "category" : product.category,
            "unit_price" : product.price,
            "quantity" : product.quantity
             "supplier" : product.product })
    with open("products.json","w") as file:
        json.dump(data, file, indent=4)
def load_products():
    try:
        with open("products.json","r") as file:
                data = json.load(file)
    except FileNotFoundError:
                return[]
                  
    products = []
    for item in data:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"]
                )
                products.append(product)
    return products

