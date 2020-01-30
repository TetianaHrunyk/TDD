class Deck:
    """
    Creates a standard deck of cards,
    represented by a list.
    """
    def __init__(self):
        self.deck = []
        for value in range(1, 14):
            for times in range(4):
                self.deck.append(value)
    
    def pull(self, n: int):
        """
        Pulling n cards. Return a list
        """
        if n > len(self.deck):
            raise ValueError("The number of cards you want to pull is greater than the current number of cards the deck contains")
        else:
            import random
            pulled = []
            for i in range(n):
                card_to_be_pulled = random.choice(self.deck)
                self.deck.remove(card_to_be_pulled)
                pulled.append(card_to_be_pulled)
            return pulled


class TopCard:
    """
    Using the Deck class, we simulate
    pulling 5 cards in the hand and
    dividing the rest into three piles.
    
    Piles are represented as a dictionary, where key is the id,
    and the value is the lsit of the cards a pile contains.
    
    Returns list in the form [PileId, PlayerCard]
    """
    
    def __init__(self, piles = 3, in_hand = 5):
        
        assert type(piles) == int
        assert type(in_hand) == int
        assert piles + in_hand <= 52
        assert piles >= 1
        assert in_hand >= 1
        
        self.deck = Deck()
        self.in_hand = self.deck.pull(in_hand)
        self.piles = {}
        
        cards_in_pile = len(self.deck.deck)//piles
        for i in range(piles):
            self.piles[i] = self.deck.pull(cards_in_pile)
        if len(self.deck.deck) > 0:
            for i in range(len(self.deck.deck)):
                self.piles[i].append(*self.deck.pull(1))
            
    def game_round(self):
        """
        Acts according to the following rules:
        1. First you put your card
        2. Then you start flipping the top cards in the piles one by one
        3. If at some point you found the cards that is less that your card
           or equals to it, you won. [PileId, PlayerCard] is returned.
        4. If none of the top cards in the piles is less then your card and 
           does not equal it, you pick the next card and start flipping 
           the second row of the top cards in the piles.
        5. This process continues until you find a card that is either 
           less or equal to your card.
        """
        for player_card in self.in_hand:
            for PileId, PileCards in self.piles.items():
                top_card = PileCards.pop(0)
#                print("Player card: ", player_card)
#                print("Top card in the pile: ", top_card)
                if player_card >= top_card:
                    return [PileId, player_card]
                
#for i in range(10):
#    print("Trial ", i)
#    game = TopCard()
#    game.game_round()
                