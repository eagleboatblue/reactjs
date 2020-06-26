import json

"""
add representation dump object self as json
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