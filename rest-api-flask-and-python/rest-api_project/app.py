from flask import Flask, request
from flask_api import status

app = Flask(__name__)

stores = [
    {
        "name": "mystore",
        "items": [
            {
                "name": "Chair",
                "price": "200"
            }
        ]
    }
]


STORE_NOT_FOUND = "Store not Found"


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"error": status.HTTP_404_NOT_FOUND, "message": STORE_NOT_FOUND}, status.HTTP_404_NOT_FOUND


@app.get("/store/<string:name>/item")
def get_store_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"error": status.HTTP_404_NOT_FOUND, "message": STORE_NOT_FOUND}, status.HTTP_404_NOT_FOUND


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, status.HTTP_201_CREATED


@app.post("/store/<string:name>/item")
def add_items(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, status.HTTP_201_CREATED
    return {"error": status.HTTP_404_NOT_FOUND, "message": STORE_NOT_FOUND}, status.HTTP_404_NOT_FOUND


if __name__ == "__main__":
    app.run(debug=True)
