from database import Database


class InventoryService:
    def __init__(self):
        self.db = Database()

    
    def get_all_products(self):
        return self.db.get_all_products()
        

    def find_product_by_id(self, product_id):
        return self.db.find_product_by_id(product_id)
    
        # VERIFICA DACA EXISTA DEJA PRODUSUL 
    def add_product(self, product):
        existing_product = self.db.find_product_by_id(product.id)
        
        if existing_product:                
            return False
        self.db.insert_product(product) 

        return True
    
    def delete_product(self,product_id):
        product = self.db.find_product_by_id(product_id)

        if product:
            self.db.delete_product(product_id)
            return True
        

        return False
    
    def add_stock(self, product_id, quantity_to_add):
        product = self.db.find_product_by_id(product_id)

        if product:
            new_quantity = product.quantity + quantity_to_add
            self.db.update_product_stock(
                product_id,
                new_quantity
                )
            

            return True
        
        return False
    

    def set_stock(self, product_id, new_quantity):
        product = self.db.find_product_by_id(product_id)

        if product:
            self.db.update_product_stock(
                product_id,
                new_quantity
            )

            return True

        return False


    def get_low_stock_products(self):
        products=self.db.get_all_products()
        low_stock_products = []
        for product in products:
            if product.is_low_stock():
                low_stock_products.append(product)

        return low_stock_products
            
    def get_out_of_stock_products(self):
        products = self.db.get_all_products()

        out_of_stock_products = []

        for product in products:
            if product.quantity == 0:
                out_of_stock_products.append(product)

        return out_of_stock_products

    def get_total_inventory_value(self):
        products = self.db.get_all_products()

        total_value = 0

        for product in products:
            total_value += product.get_inventory_value()

        return total_value