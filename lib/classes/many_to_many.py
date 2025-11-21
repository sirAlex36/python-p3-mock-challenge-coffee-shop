class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Coffee name cannot be changed after initialization.")

        if not isinstance(value, str):
            raise TypeError("Name must be a string.")  

        if len(value) < 3:
            raise ValueError("Name must be atleast 3 characters long.") 

        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0  
        total = sum(order.price for order in orders)
        return total / len(orders)

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be sa string.")
        
        if not(1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")

        self._name = value

        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
      
        if hasattr(self, "_price"):
            raise AttributeError("Order price cannot be changed after initialization.")

        if not isinstance(value, float):
            raise TypeError("Price must be a float.")

        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0 inclusive.")

        self._price = value