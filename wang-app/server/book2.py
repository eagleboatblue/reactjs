import json

"""
add total price function to calculate total price
"""
class book:
    def __init__(self, values:dict=None):
        self.title = values.get('title')
        self.price = values.get('price')
    
    def __repr__(self):
        return json.dumps(self.__dict__)

    def getTitle(self):
        return self.title

    def getPrice(self):
        return self.price

def totalPrice(bookList:book):
    total = 0
    for i in bookList:
        price = i.getPrice()
        total += price
    return total
