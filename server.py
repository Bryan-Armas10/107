from flask import Flask, request, abort
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # warning this disables CORS policy

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

#############################################################################################################
#############################################################################################################

products = []
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def get_products():
    products_db = []
    cursor = db.products.find({})
    for prod in cursor:
        products_db.append(fix_id(prod))
    return json.dumps(products_db)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    # products.append(item)
    db.products.insert_one(item)
    return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item = request.get_json()
    if 0 <= index <= len(products):
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "That index does not exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_item = request.get_json()
    if 0 <= index <= len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "That index does not exist" 

# pacth -- the method to update an especific element into python is: list.update

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field = request.get_json()
    if 0 <= index <= len(products):
        updated_field(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"



################################

##########  COUPONS   ############

##################################

 

# post /api/coupons
# save coupons into a db.coupons collection
@app.post("/api/coupons")
def save_coupon():
    item = request.get_json()
    db.coupons.insert_one(item)
    return json.dumps(fix_id(item))


@app.get("/api/coupons")
def get_coupon():
    coupons = []
    cursor = db.coupons.find({})
    for cp in cursor:
        coupons.append(fix_id(cp))
        return json.dumps(coupons) 

@app.get("/api/coupons/<code>")
def validate_coupon(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon == None:
        print("Error: invalid coupon")
        return abort(404, "Invalid code")
    
    return json.dumps(fix_id(coupon))


# Run the Flask server
app.run(debug=True)
