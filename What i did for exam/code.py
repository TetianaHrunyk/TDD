class Seller:
    
     def __init__(self, price, discount_perc, discount_kg):
        self.price = price
        self.discount_perc = discount_perc
        self.discount_kg = discount_kg

class AppleMarket:
    
    def __init__(self):
        self.seller1 = Seller(200, [10], [10])
        self.seller2 = Seller(199, [0], [0])
        self.seller3 = Seller(250, [5, 10, 20], [10, 20, 100])
        
    def GetPrice(self, kg):
        if kg >= self.seller1.discount_kg[0]:
            price1 = kg * self.seller1.price * (1-(self.seller1.discount_perc[0]/100))
        else:
            price1 = kg * self.seller1.price
            
        if kg >= self.seller2.discount_kg[0]:
            price2 = kg * self.seller2.price * (1-(self.seller2.discount_perc[0]/100))
        else:
            price2 = kg * self.seller2.price
            
        
        
        if kg >= self.seller3.discount_kg[0]:
            price3 = kg * self.seller3.price * (1-(self.seller3.discount_perc[0]/100))
        else:
            price3 = kg * self.seller3.price
            
        if kg >= self.seller3.discount_kg[1]:
            price3 = kg * self.seller3.price * (1-(self.seller3.discount_perc[1]/100))
        else:
            price3 = kg * self.seller3.price
            
        if kg >= self.seller3.discount_kg[2]:
            price3 = kg * self.seller3.price * (1-(self.seller3.discount_perc[2]/100))
        else:
            price3 = kg * self.seller3.price
            
        if min(price1, price2, price3) == price1:
            return ["Seller1", round(price1)]
        elif min(price1, price2, price3) == price2:
            return ["Seller2", round(price2)]
        else:
            return ["Seller3", round(price3)]
    
    