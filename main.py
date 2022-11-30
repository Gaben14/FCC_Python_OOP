class Item:
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

    def calculate_total_price(self):
        return self.price * self.quantity

if __name__ == '__main__':
    print('PyCharm')

    item1 = Item("Phone", 100, -1) # Creating a new instance of the Item class
    item2 = Item("Laptop", 1000, 3)  # Creating a new instance of the Item class
    #Calling the calculate_total_price() method for both instances.
    print(item1.calculate_total_price())
    print(item2.calculate_total_price())
