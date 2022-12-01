import csv

class Item:
    pay_rate = 0.8 # Class Attribute
    all = [] # List to store all the instances that have been created
    #Constructor creation
    def __init__(self, name: str, price: int, quantity=0):
        # Assert validation - Run validations to the received arguments
        assert price >= 0, f"Price {price} should be greater than or equal to 0 (zero)"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to 0 (zero)"

        # Assign to self object
        # The self.name will be equal to the name value of each new instance.
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) # self is the instance itself

    @property
    # @property decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    # We need to use the Instance class, if the instance does not have the specific attribute
    # it will look up for the class level attribute

    @classmethod
    def instatiate_from_something(cls):
        '''
        This should also do somethingt that has a relationship
        with the class, but usually, those are used to manipulate
        different structures of data to instantiate objects,
        like we have done with CSV.
        '''

    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship with the class,
        but not something that must be unique per instance!

        Static methods are not passing the object reference as the first
        argument in the background (classmethods use cls)
        '''

    # With the __repr__ we can specify the way we want to represent our object, when printing it out
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @property # Creating a read-only property
    def read_only_name(self):
        return "AAA"