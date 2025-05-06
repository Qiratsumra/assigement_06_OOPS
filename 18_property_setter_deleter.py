# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product :
    def __init__(self,price):
        self.__price = price
    # @property to get the price
    @property
    def get_price(self):
        return self.__price
    # used @price.setter to update it because price is private property
    @get_price.setter
    def get_price(self,price):
        try:
            self.__price = price
            print(f'Updated Price is {price}')
        except:
            price(ValueError)
    # @price.deleter to delete it.
    @get_price.deleter
    def get_price(self):
        print('Deleting price....')
        del self.__price

item1 = Product(300) #access the price 
item1.price = 300 #updating the price
print(item1.price) 
del item1.price #delete the price
print(item1.price) #get error