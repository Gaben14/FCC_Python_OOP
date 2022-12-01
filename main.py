import csv

class Item:
    pay_rate = 0.8 # Class Attribute
    all = [] # List to store all the instances that have been created
    #Constructor creation
    def __init__(self, name: str, price: int, quantity: int):
        # Assert validation - Run validations to the received arguments
        assert price >= 0, f"Price {price} should be greater than or equal to 0 (zero)"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to 0 (zero)"

        # Assign to self object
        # The self.name will be equal to the name value of each new instance.
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) # self is the instance itself

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
    # We need to use the Instance class, if the instance does not have the specific attribute
    # it will look up for the class level attribute

    # With the __repr__ we can specify the way we want to represent our object, when printing it out
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

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

if __name__ == '__main__':
    phone1 = Phone('jscPhonev10',500,5)
    phone2 = Phone('jscPhonev20',700,5)

    print(phone1.broken_phones)

