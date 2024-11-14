from flask import Flask, request
import json

app = Flask(__name__)

# Welcome page (root)
@app.get("/")
def home():
    return """
    <h1>Welcome to the Product API</h1>
    <p>Use the following endpoints:</p>
    <ul>
        <li><b>/about</b> - About page</li>
        <li><b>/api/products</b> - Get all products</li>
        <li><b>/api/products/count</b> - Get product count</li>
    </ul>
    """

# About Page
@app.get("/about")
def about():
    return """
    <h1>About This API</h1>
    <p>This API is designed to manage a product catalog.</p>
    <p>It allows you to get, add, update, and delete products.</p>
    """

# Product List
products = []

@app.get("/api/products")
def get_products():
    return json.dumps(products)

# Count products
@app.get("/api/products/count")
def get_product_count():
    return json.dumps({"count": len(products)})

# Save a new product (POST)
@app.post("/api/products")
def save_product():
    item = request.get_json()
    print(item)
    products.append(item)
    return json.dumps(item)

# Update a product (PUT)
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_item = request.get_json()
    if 0 <= index < len(products):
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "That index does not exist"

# Delete a product (DELETE)
@app.delete("/api/products/<int:index>")
def delete_product(index):
    if 0 <= index < len(products):
        deleted_item = products.pop(index)
        return json.dumps(deleted_item)
    else:
        return "That index does not exist"

# Partially update a product (PATCH)
@app.patch("/api/products/<int:index>")
def patch_product(index):
    updated_field = request.get_json()
    if 0 <= index < len(products):
        products[index].update(updated_field)
        return json.dumps(products[index])
    else:
        return "That index does not exist"

# Run the Flask server
app.run(debug=True)