class AppleMarket:
    
    def __init__(self, price = 0):
        assert price >= 0
        self.price = price
        
    def getPrice(self, amount):        
        assert amount >= 0
        return self.price * amount
    
    def getDiscount(self, amount):
        assert amount >= 10        
        return self.price * amount * 0.9        
    