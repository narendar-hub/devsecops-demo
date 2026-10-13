from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Keyboard", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 600},
    {"id": 3, "name": "Headphones", "price": 1800}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to ShopKart!"})

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
