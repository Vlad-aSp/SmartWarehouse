from flask import Flask, render_template,request,redirect
from service import InventoryService
from product import Product

app = Flask(__name__)

service = InventoryService()

@app.route("/")
def home():

    products = service.get_all_products()

    return render_template(
        "index.html",
        products=products
    )

@app.route("/add_product", methods=["POST"])
def add_product():

    name = request.form["name"]
    category = request.form["category"]
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])
    minimum_stock = int(request.form["minimum_stock"])

    products = service.get_all_products()

    if products:
        new_id = max(product.id for product in products) + 1
    else:
        new_id = 1

    product = Product(
        new_id,
        name,
        category,
        quantity,
        price,
        minimum_stock
    )

    service.add_product(product)

    return redirect("/")
@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    service.delete_product(product_id)
    return redirect("/")


@app.route("/edit_stock/<int:product_id>")
def edit_stock(product_id):
    product = service.find_product_by_id(product_id)

    return render_template(
        "edit_stock.html",
        product=product
    )

@app.route("/update_stock/<int:product_id>", methods=["POST"])
def update_stock(product_id):

    new_quantity = int(request.form["new_quantity"])

    service.set_stock(
        product_id,
        new_quantity
    )

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)