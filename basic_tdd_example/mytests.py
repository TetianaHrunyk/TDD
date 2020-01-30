import unittest
from mycode import *

class MyFirstTest(unittest.TestCase):
    
#    def setUp(self):
#        print("We are about to start")
#        
#    def tearDown(self):
#        print("We have just finished")
    
    def test_hello(self):
        self.assertEqual(hello_world(), "hello world")
        
    def test_list(self):
        self.assertEqual(len(create_list(10)), 10)
        a = create_list(10)
        self.assertGreater(a[9], a[0])
        

if __name__ == '__main__':
    unittest.main()