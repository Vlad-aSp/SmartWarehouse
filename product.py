class Product:

    def __str__(self):
        return f"ID: {self.id}, Name: { self.name}, Quantity: { self.quantity}"  # RETURNEAZA ID,NUME,CANTITATE CAND ESTE RETURNAT PRODUSUL (return product)

    """Am creat clasa 'Product' """

    def __init__(
            self,
            id: int,            #ADAUGAT TIPURILE DE DATE 
            name: str,
            category: str,
            quantity: int,
            price: float,
            minimum_stock: int,
    ):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.minimum_stock = minimum_stock
        

    """Verificare cantitate stock"""


    def is_low_stock(self):
         return self.quantity <= self.minimum_stock
    

    """PRELUAM VALOAREA PRODUSULUI"""

    def get_inventory_value(self):
        return self.quantity * self.price     
    






