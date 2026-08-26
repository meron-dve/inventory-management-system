import json
#from products import Product
def save_products(products):
    data = []

    for product in products:
        data.append({
            "product_id": product.product_id,
            "name" : product.name,
            "category" : product.category,
            "price" : product.price,
            "quantity" : product.quantity })
    with open("products.json","w") as file:
        json.dump(data, file, indent=4)
    def load_products():
        with open("products.json","r") as file:
            data = json.load(file)
            print(data)
            for item in data:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"]
                )
            