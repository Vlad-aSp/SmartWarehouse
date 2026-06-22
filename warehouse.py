class Warehouse:
    def __init__(self):
        self.products= [] # LISTA DE PRODUSE


    """Adaugare produse"""

    def add_product(self,product):
        self.products.append(product)


    """Cautare dupa ID"""

    def find_product_by_id(self,product_id):
        for product in self.products:       #PARCURGEREA LISTEI
            if product.id == product_id:    #DACA ID - UL ESTE GASIT 
                return product              #RETURNEAZA NUMELE 
        
        return None
    

    """Eliminare dupa ID"""

    def remove_product(self,product_id):
        product = self.find_product_by_id(product_id)  #GASIM PRODUSUL DUPA ID

        if product:                                    #DACA ESTE GASIT
            self.products.remove(product)              #ELIMINAM DIN LISTA
            return True
        
        return False
    

    """Adauga stock"""

    def add_stock(self,product_id,to_add_quantity):
        product= self.find_product_by_id(product_id)

        if product:
            product.quantity += to_add_quantity        #CANTITATE VECHE + CANTITATE NOUA
            return product
        return False
    

    """Schimba valoarea stock ului """
    
    def new_stock(self,product_id,new_quantity):
        product = self.find_product_by_id(product_id)

        if product:
            product.quantity = new_quantity            #CANTITATEA VECHE DEVINE CANTITATEA NOUA
            return product
        return False
    
    """Preia tot produsele care au stock ul scazut"""
    
    def get_low_stock_products(self):
        low_stock_products=[]                       #LISTA PENTRU PRODUSE CU STOCK MIC

        for product in self.products:   
            if product.is_low_stock():              #VERIFICA DACA STOCK UL ESTE MIC 
                low_stock_products.append(product)  #ADAUGA IN LISTA DE MAI SUS 

        return low_stock_products                   #RETUENEAZA LISTA
            
            