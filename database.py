import sqlite3
from product import Product

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("warehouse.db" ,check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        quantity INTEGER,
        price REAL,
        minimum_stock INTEGER
    )
    """)

        self.connection.commit()


    def insert_product(self, product):
        self.cursor.execute("""
    INSERT INTO products                                    
    (id, name, category, quantity, price, minimum_stock)
    VALUES (?, ?, ?, ?, ?, ?)                               
    """,
    (
        product.id,
        product.name,
        product.category,
        product.quantity,
        product.price,
        product.minimum_stock
    ))

        self.connection.commit() 
    
    def get_all_products(self):
        self.cursor.execute("SELECT * FROM products")

        rows = self.cursor.fetchall()
    
        products=[]

        for row in rows:
            product = Product(
                row[0], #ID 
                row[1], #NAME
                row[2], #CATEGORY
                row[3], #QUANTITY
                row[4], #PRICE
                row[5]  #MINIMUM_STOCK
            )

            products.append(product)

        return products
            
    def delete_product(self, product_id,):
        self.cursor.execute("""
    DELETE FROM products
    WHERE id = ?
    """, (product_id,))

        self.connection.commit() 

    def update_product_stock(self, product_id, new_quantity):
        print("UPDATE EXECUTED")
        self.cursor.execute("""
            UPDATE products
            SET quantity = ? 
            WHERE id = ?
            """, (new_quantity,product_id))

        self.connection.commit()       

    def find_product_by_id(self, product_id):
        self.cursor.execute("""
    SELECT * FROM products
    WHERE id = ?
    """, (product_id,))

        row = self.cursor.fetchone()

        if row:
            product = Product(
                row[0],  # ID
                row[1],  # NAME
                row[2],  # CATEGORY
                row[3],  # QUANTITY
                row[4],  # PRICE
                row[5]   # MINIMUM_STOCK
        )

            return product

        return None
            