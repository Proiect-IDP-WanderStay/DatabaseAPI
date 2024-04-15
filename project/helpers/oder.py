class Order:
    def __init__(self) -> None:
        self.alphabetic = 1
        self.price = 1

    def read_order(self, json):
        if not json:
            return self
        
        if ('alphabetic' in json):
            self.alphabetic = json['alphabetic']
        if ('price' in json):
            self.price = json['price']
