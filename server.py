from flask import Flask
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
def abouutGet():
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

app.run(debug=True)