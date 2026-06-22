from product import Product
from warehouse import Warehouse

product = Product(
    1,              #ID
    "Laptop",       #NUME
    "Electronics",  #CATEGORIE
    0,             #STOCK
    3500,           #PRET
    3
)
product2 = Product(
    2,
    "Mouse",
    "Electronics",
    0,
    100,
    5
)

product3 = Product(
    3,
    "Headphones",
    "Electronics",
    10,
    250,
    5
)

print(product.name)
print(product.quantity)
print(product.price)
print(product.is_low_stock())

warehouse = Warehouse()
warehouse.add_product(product)
warehouse.add_product(product2)
warehouse.add_product(product3)
print(warehouse.products)
print(len(warehouse.products))

#found_product = warehouse.find_product_by_id(1)

#if found_product:
    #print(found_product.name)

#warehouse.remove_product(1)
#print(len(warehouse.products))
#print("Test")
#for product in warehouse.products:
    #print(product.id, product.name)

#print(warehouse.add_stock(1,1))

#print(warehouse.new_stock(1,20))

low_stock = warehouse.get_low_stock_products()

for product in low_stock:
    print(product)

print(warehouse.get_total_inventory_value())


zero_stock = warehouse.get_out_of_stock_products()

for product in zero_stock:
    print(product)