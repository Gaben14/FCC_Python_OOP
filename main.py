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

if __name__ == '__main__':
    print('PyCharm')

    #item1 = Item("Phone", 100, 1) # Creating a new instance of the Item class
    #item2 = Item("Laptop", 100, 1)  # Creating a new instance of the Item class
    #Calling the calculate_total_price() method for both instances.
    #print(item1.calculate_total_price())
    #print(item2.calculate_total_price())

    #print(Item.pay_rate) # Accessing the Class Attribute
    #print(f"item1 {item1.pay_rate} ")
    #print(f"item2 {item2.pay_rate} ")

    #item1.apply_discount()
    #print(f"item1.price {item1.price}") #Class Level attribute

    #item2.pay_rate = 0.7 #Instance level attribute creation
    #item2.apply_discount()
    #print(f"item2.price {item2.price}")

    item1 = Item("Phone", 100, 1)
    item2 = Item("Laptop", 1000, 3)
    item3 = Item("Cable", 10, 5)
    item4 = Item("Mouse", 50, 5)
    item5 = Item("Keyboard", 75, 5)

    print(Item.all)

