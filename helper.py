# When to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship with the class,
        but not something that must be unique per instance!

        Static methods are not passing the object reference as the first
        argument in the background (classmethods use cls)
        '''

    @classmethod
    def instatiate_from_something(cls):
        '''
        This should also do somethingt that has a relationship
        with the class, but usually, those are used to manipulate
        different structures of data to instantiate objects,
        like we have done with CSV.
        '''