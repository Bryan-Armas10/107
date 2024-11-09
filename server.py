from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"
# this is an example
# @app.post("/")
#def homePost():
#    return "hello from the test server"

# Endpoints
@app.get("/test")
def text():
    return "hello from the test server"

# endPoint using json
app.get("/api/about")
def aboutGet():
    name = {"name": "Adrian"}
    return json.dumps(name)

# create a new route /greet/{name}, this route should accept name
# as part  of the url and return an htmo message saying hello {name}

@app.get("/greet/<name>")
def greet(name):
    return f"""
    <h1 style=color:blue>Hello {name}!</h1>"""

# by creating the farewell message
@app.get("/farewell/<name>")
def farewell(name):
    return f"""
    <h1 style=color:blue>bye bye {name}!</h1>"""

# ###############################################
products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    products.append(item)
    return json.dumps(item)

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
        delete_products = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "That index does not exist"

# pacth -- the method to update an especific element  into python is: list.update

@app.patch("/api/products/<int:index>")
def patch_products(index):
    updated_field = request.get_json()
    if 0 <= index <= len(products):
        updated_field(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"

app.run(debug=True)