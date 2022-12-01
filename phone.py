from item import Item # importing the item class

class Phone(Item):
    # Constructor in the child class, the last items inside the __init__ should be the
    # child class' own items.
    def __init__(self, name: str, price: int, quantity: int, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments:
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to 0(zero)"

        #Assign to self object
        self.broken_phones = broken_phones