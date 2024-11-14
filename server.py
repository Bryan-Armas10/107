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
        <li><b>/api/catalog</b> - Get all products in the catalog</li>
        <li><b>/api/catalog</b> - Add new product to the catalog</li>
        <li><b>/api/reports/total</b> - Get the total value of all products</li>
        <li><b>/api/products/{category}</b> - Get products by category</li>
    </ul>
    """

# About Page
@app.get("/about")
def about():
    return """
    <h1>About This API</h1>
    <p>This API allows you to manage a product catalog. You can add, view, update, and delete products, as well as view reports.</p>
    """

# Products list
products = []

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(products)

@app.post("/api/catalog")
def save_product():
    item = request.get_json()
# Check if the product has the required fields
    if 'name' not in item or 'price' not in item or 'category' not in item:
        return "Product must have 'name', 'price', and 'category'.", 400
    products.append(item)
    return json.dumps(item), 201

@app.get("/api/reports/total")
def get_total_value():
    total_value = sum(product['price'] for product in products if 'price' in product)
    return json.dumps({"total_value": total_value})

@app.get("/api/products/<category>")
def get_products_by_category(category):
    filtered_products = [product for product in products if product.get('category') == category]
    return json.dumps(filtered_products)

# Run the Flask server
app.run(debug=True)
