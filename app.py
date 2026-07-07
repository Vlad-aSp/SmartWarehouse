from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
)
from service import InventoryService
from product import Product

app = Flask(__name__)

app.secret_key = "smartwarehouse"

service = InventoryService()

@app.route("/")
def home():
    print("HPME ROUTE")
    search_text = request.args.get("search", "")

    if search_text:
        products= service.search_products(search_text)
    else:
        products = service.get_all_products()

    total_products = len(products)

    inventory_value = service.get_total_inventory_value()

    low_stock_products = service.get_low_stock_products()

    out_of_stock_products = service.get_out_of_stock_products()

    return render_template(
        "index.html",
        products=products,
        total_products=total_products,
        inventory_value=inventory_value,
        low_stock_products=low_stock_products,
        out_of_stock_products=out_of_stock_products
    )





@app.route("/add_product", methods=["POST"])
def add_product():

    name = request.form["name"].strip()
    category = request.form["category"].strip()
    quantity = request.form["quantity"].strip()
    price = request.form["price"].strip()
    minimum_stock = request.form["minimum_stock"].strip()

    

    if not name:
        flash("Product name is required!")
        return redirect("/")

    if not category:
        flash("Category is required!")
        return redirect("/")

    if not quantity:
        flash("Quantity is required!")
        return redirect("/")

    if not price:
        flash("Price is required!")
        return redirect("/")

    if not minimum_stock:
        flash("Minimum stock is required!")
        return redirect("/")

    quantity = int(quantity)
    price = float(price)
    minimum_stock = int(minimum_stock)

    if quantity < 0:
        flash("Quantity cannot be negative!")
        return redirect("/")

    if price < 0:
        flash("Price cannot be negative!")
        return redirect("/")

    if minimum_stock < 0:
        flash("Minimum stock cannot be negative!")
        return redirect("/")

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

    flash("Product added successfully!")

    return redirect("/")




@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    service.delete_product(product_id)
    flash("Product deleted successfully!")
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
    flash("Stock updated successfully!")
    return redirect("/")

@app.route("/add_stock/<int:product_id>", methods=["POST"])
def add_stock(product_id):

    quantity_to_add = int(request.form["quantity_to_add"])

    service.add_stock(
        product_id,
        quantity_to_add
    )
    flash("Stock added successfully!")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)