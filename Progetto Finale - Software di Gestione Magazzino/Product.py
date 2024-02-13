class Product:
    """
    This class represents a shop product. 
    """
    
    def __init__(self,name,sale_price,purchase_price,quantity):
        """
        Class constructor.
        Input:
        - name (str): product's name.
        - sale_price (float): sale price.
        - purchase_price (float): purchase price.
        - quantity (int): product's quantity available in the shop.
        """
        
        self._name = name
        self._sale_price = sale_price
        self._purchase_price = purchase_price
        self._quantity = quantity 
        
        
    def __repr__(self):
        """
        Override of special method repr, in order to get a custom string format
        of the instances.
        """
        info = "{:<15} | {:<8} | {:<.2f}".format(
            self.get_name(),self.get_quantity(),self.get_sale_price())
        return info
    
    def __dict__(self):
        """
        Override of special method dict, in order to get a dict from the class           objects.
        """
        return {
            'name': self.get_name(),
            'sale_price': self.get_sale_price(),
            'purchase_price': self.get_purchase_price(),
            'quantity': self.get_quantity()
        }
    
    def get_name(self):
        """
        Getter for name field.
        """
        return self._name
    
    def set_name(self,name):
        """
        Setter for name field.
        """
        self._name = name
        
    def get_sale_price(self):
        """
        Getter for sale_price field.
        """
        return self._sale_price
    
    def set_sale_price(self,sale_price):
        """
        Setter for sale_price field.
        """
        self._sale_price = sale_price
        
    def get_purchase_price(self):
        """
        Getter for purchase_price field.
        """
        return self._purchase_price
    
    def set_purchase_price(self,purchase_price):
        """
        Setter for purchase_price field.
        """
        self._purchase_price = purchase_price
    
    def get_quantity(self):
        """
        Getter for quantity field.
        """
        return self._quantity
    
    def set_quantity(self,quantity):
        """
        Setter for quantity field.
        """
        self._quantity = quantity