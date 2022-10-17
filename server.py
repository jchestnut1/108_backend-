from flask import Flask
import json
from config import me, hello
from mock_data import catalog


app = Flask("Server")


@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is a test"


@app.get("/about")
def about():
    return "Jay Chestnut"



@app.get("/api/version")
def version():
    v = {
        "version": "1.0.0",
        "build": 21,
        "name": "Gore 3",
        "developer": me
    }

    hello()

    return json.dumps(v)


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


@app.get("/api/products/count")
def total_count():
    return json.dumps( len(catalog))




app.run(debug=True)