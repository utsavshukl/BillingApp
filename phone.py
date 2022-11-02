from bill import Bill


class Phone(Bill):
    def __init__(self, product : str, price :float, quantity = 0, broken_phones = 0): 
        all = []
        super().__init__(
            product, price, quantity
        ) 
        # Validation
        assert broken_phones >= 0, f"Broken phones {broken_phones} is a negative number"  
        # Actions to execute
        Phone.all.append(self)
        def __repr__(self):
            return f"[{product}, {price}, {quantity}, {broken_phones}]"
