import csv

class Bill:
    discount = 0.2
    all = []
    def __init__(self, product : str, price : float, quantity):
        #validations
        assert price >= 0, f"Price {price} is not greater then zero."
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero."
        
        #assignment of objects
        self._product = product
        self.price = price
        self.quantity = quantity

        Bill.all.append(self)
    
    # Locking the values of some critical values
    @property
    def name(self):
        return self._product

    def calc(self):
        print(f"The total bill is {self.price*self.quantity}")
    
    def apply_discount(self):
        self.price = self.price - (self.price * Bill.discount)
    
    # ClassMethod
    @classmethod
    def instantiae_from_csv(cls):
        with open ('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for i in items:
            Bill(
                product = i.get('name'),
                price = float(i.get('price')),
                quantity = int(i.get('quantity'))
            )
    
    # StaticMethod
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):            
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"Item [{self.product}, {self.price}, {self.quantity}]"

 