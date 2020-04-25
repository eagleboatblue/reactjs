import json

"""
Simple book class.
"""
class book:
    def __init__(self, values:dict=None):
        self.title = values.get('title')
        self.price = values.get('price')
    
    def getTitle(self):
        return self.title

    def getPrice(self):
        return self.price

