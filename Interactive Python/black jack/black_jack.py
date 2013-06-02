# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
player_hand = None
dealer_hand = None
dealer_deck = None
pos = [11, 310]
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        s = 'Hand contains '
        for card in self.hand:
            s += str(card) + ' '
        return s
    
    def add_card(self, card):
        self.hand.append(card)
    def __calculate_value(self):
        value = 0
        has_ace = False
        for card in self.hand:
            if (card.get_rank() == 'A'):
                has_ace = True
            value += VALUES[card.get_rank()]
        if (has_ace and (value + 10 <= 21)):
            return value + 10
        else:
            return value

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        return self.__calculate_value()
   
    def draw(self, canvas, pos):
        for card in self.hand:
            pos = (pos[0] + 74, pos[1])
            card.draw(canvas, pos)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(SUITS[suit], RANKS[rank]) for suit in range(4) for rank in range(13)] # create a Deck object

    def shuffle(self):
        return random.shuffle(self.deck) # use random.shuffle() to shuffle the deck

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        s = 'Deck contains ' # return a string representing the deck
        
        for card in self.deck:
            s += str(card) + ' '
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, dealer_deck, score
    if not in_play:
        dealer_deck = Deck()
        dealer_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(dealer_deck.deal_card())
        print 'Player ' + str(player_hand)
        dealer_hand.add_card(dealer_deck.deal_card())
        print 'Dealer ' + str(dealer_hand)
        player_hand.add_card(dealer_deck.deal_card())
        print 'Player ' + str(player_hand)
        dealer_hand.add_card(dealer_deck.deal_card())
        print 'Dealer ' + str(dealer_hand)
        outcome = "Hit or Stand?"
        in_play = True
    else:
        score -= 1
        in_play = False
        deal()

def hit():
    global outcome, player_hand, in_play, score
    # if the hand is in play, hit the player
    if in_play:
        if (player_hand.get_value() <= 21):
            player_hand.add_card(dealer_deck.deal_card())
            print 'Player ' + str(player_hand)
        
            if (player_hand.get_value() > 21):
                in_play = False
                score -= 1
                outcome = 'You have BUSTED!'
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, player_hand, dealer_hand, dealer_deck, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if (player_hand.get_value() > 21):
        print 'You have BUSTED!'
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(dealer_deck.deal_card())
            print 'Dealer ' + str(dealer_hand)
        if in_play:
            if (dealer_hand.get_value() > 21):
                score += 1
                in_play = False
                outcome ='Dealer have BUSTED! - Player Wins!'
            elif (dealer_hand.get_value() < player_hand.get_value()):
                score += 1
                in_play = False
                outcome ='Player Wins!'
            else:
                score -= 1
                in_play = False
                outcome = 'Dealer Wins!'

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand
    canvas.draw_text("Black Jack", (245, 70), 80, "Black")
    canvas.draw_text(outcome, (350, 143), 25, "Black")
    canvas.draw_text("Score", (370, 520), 30, "Black")
    canvas.draw_text(str(score), (402, 550), 20, "Black")
    canvas.draw_text("Dealer", (100, 120), 45, "Black")
    canvas.draw_text("Player", (100, 470), 45, "Black")
    player_hand.draw(canvas, pos)
    dealer_hand.draw(canvas, (pos[0], pos[1] - 160))
    if (in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (pos[0] + 110, pos[1] - 111), CARD_SIZE)
            


# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()
