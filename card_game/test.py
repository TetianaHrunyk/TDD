import unittest
from code import *

class DeckTest(unittest.TestCase):
    
    def test_init(self):
        """
        Tests if the deck contains valid number of cards, which is 52.
        """
        mydeck = Deck()
        self.assertEqual(len(mydeck.deck), 52)
        
    def test_pulling(self):
        mydeck = Deck()
        pulled = mydeck.pull(5)
        self.assertEqual(len(pulled), 5)
        
    def test_deck_after_pulling(self):
        """
        Tests if the number of cards in the deck
        decreases after pulling some cards
        """
        mydeck = Deck()
        initial_num_of_cards = len(mydeck.deck)
        mydeck.pull(5)
        self.assertEqual(len(mydeck.deck), initial_num_of_cards - 5)
        
    def test_cards_pulled(self):
        """
        Tests if only the cards we pulled are removed from the deck.
        """
        mydeck = Deck()
        initial_deck = mydeck.deck
        pulled = mydeck.pull(5)
        for p in pulled:
            initial_deck.remove(p)
        self.assertEqual(mydeck.deck, initial_deck)
        
    @unittest.expectedFailure
    def test_pulling_with_invalid_card_number(self):
        """
        Tests the program's behaviour when we are trying
        to pull more cards that the deck contains.
        """
        mydeck = Deck()
        mydeck.pull(60)
        
class TopCardTest(unittest.TestCase):
    
    def test_game_round_return_value(self):
        game = TopCard()
        result = game.game_round()
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 2)
        self.assertEqual(type(result[0]), int)
        self.assertEqual(type(result[1]), int)
        
    def test_init_with_valid_values(self):
        """
        Test if the TopCard class can be instantiated with
        with different sets of valid values
        """
        game = TopCard(5, 10)
        #make sure nothing is left in the deck
        self.assertEqual(len(game.deck.deck), 0)
        #make sure none of the piles is empty
        for cards in game.piles.values():
         self.assertNotEqual(len(cards), 0)
        
        game = TopCard(1, 51)
        self.assertEqual(len(game.deck.deck), 0)
        for cards in game.piles.values():
         self.assertNotEqual(len(cards), 0)
        
        game = TopCard(51, 1) 
        self.assertEqual(len(game.deck.deck), 0)
        for cards in game.piles.values():
         self.assertNotEqual(len(cards), 0)
        
    @unittest.expectedFailure
    def test_init_with_invalid_values1(self):
        game = TopCard(0, 10)
        
    @unittest.expectedFailure
    def test_init_with_invalid_values2(self):
        game = TopCard(1, 0)
        
    @unittest.expectedFailure
    def test_init_with_invalid_values3(self):
        game = TopCard(45, 45)
        
    @unittest.expectedFailure
    def test_init_with_invalid_values4(self):
        game = TopCard(2, 100)
        
    @unittest.expectedFailure
    def test_init_with_invalid_values5(self):
        game = TopCard("card", 45)
        
    @unittest.expectedFailure
    def test_init_with_invalid_values6(self):
        game = TopCard(2, "card")
        

if __name__ == '__main__':
    unittest.main()