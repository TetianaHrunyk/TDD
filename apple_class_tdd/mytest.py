import unittest
from mycode import *

class AppleMarketTest(unittest.TestCase):
        
    @unittest.expectedFailure
    def test_init_neg(self):
        market = AppleMarket(9, 45)
        
    @unittest.expectedFailure
    def test_init_price_neg(self):
        market = AppleMarket(-4)
        self.assertGreaterEqual(market.price, 0)
    
    def test_init_price_pos(self):
        market = AppleMarket()
        self.assertGreaterEqual(market.price, 0)
                
    @unittest.expectedFailure
    def test_get_price_neg(self):
        market = AppleMarket(2)
        self.assertLessEqual(market.getPrice(-1), 0)
        
    def test_get_price_pos(self):
        market = AppleMarket(2)
        self.assertGreaterEqual(market.getPrice(4), 0)
        
    @unittest.expectedFailure
    def test_get_discount_neg(self):
        market = AppleMarket(2)
        self.assertLessEqual(market.getPrice(10), market.getDiscount(10))
        
    def test_get_discount_pos(self):
        market = AppleMarket(2)
        self.assertGreaterEqual(market.getPrice(10), market.getDiscount(10))
        
    @unittest.expectedFailure
    def test_discount_validity_neg(self):
        market = AppleMarket(2)
        market.getDiscount(5)
        
    def test_discount_validity_pos(self):
        market = AppleMarket(2)
        market.getDiscount(15)
        
if __name__ == "__main__":
    unittest.main()