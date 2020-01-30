import unittest
from code import *

class AppleMarketTest(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_init_seller_neg(self):
        seller = Seller(1, 2)
        
    def test_init_seller_pos(self):
        seller = Seller(1, 2, 7)
        
    def test_initial_val_pos(self):
        market = AppleMarket()
        self.assertEqual(market.seller1.price, 200)
        
    @unittest.expectedFailure
    def test_initial_val_neg(self):
        market = AppleMarket()
        self.assertEqual(market.seller1.price, 'cheap')
        
    @unittest.expectedFailure
    def test_get_price_neg(self):
        market = AppleMarket()
        price_for2 = market.GetPrice(2)
        price_for200 = market.GetPrice(200)        
        self.assertEqual(price_for2[1], price_for200[1])
        
    def test_get_price_return_val_pos(self):
        market = AppleMarket()
        price = market.GetPrice(50)       
        self.assertEqual(len(price), 2)
        
    @unittest.expectedFailure
    def test_get_price_return_val_type0_neg(self):
        
        market = AppleMarket()
        price = market.GetPrice(50) 
        print("\n", "Return vlue test")
        print("Price for 50 kg")
        print(price[0], " ", price[1])
        self.assertEqual(type(price[0]), int)
    
    def test_get_price_return_val_type0_pos(self):
        market = AppleMarket()
        price = market.GetPrice(50)       
        self.assertEqual(type(price[0]), str)
        
    @unittest.expectedFailure
    def test_get_price_return_val_type1_neg(self):
        market = AppleMarket()
        price = market.GetPrice(50)       
        self.assertEqual(type(price[1]), str)
        
    def test_get_price_return_val_type1_pos(self):
        market = AppleMarket()
        price = market.GetPrice(50)       
        self.assertEqual(type(price[1]), int)
        
    def test_discounts_pos(self):
        market = AppleMarket()
        price_for9 = market.GetPrice(9)
        print("\n", "Discount test")
        print( "Price for 9 kg")
        print(price_for9[0], " ", price_for9[1])
        price_for10 = market.GetPrice(10)  
        print( "Price for 10 kg")
        print(price_for10[0], " ", price_for10[1])
        self.assertLess(price_for9[1], price_for10[1])
        
#    def test_discounts_pos(self):
#        market = AppleMarket()
#        price_for1000 = market.GetPrice(1000)
#        print("\n", "Discount test for big purchase")
#        print( "Price for 1000 kg")
#        print(price_for1000[0], " ", price_for1000[1])
#        self.assertEqual(price_for1000[0], "Seller1")
#        
        
        
        

if __name__ == "__main__":
    unittest.main()