class Card(object):
	"""docstring for Card"""
	def __init__(self, suit, rank):

		self.suit = suit
		self.rank = rank


	def get_suit(self):
		if self.suit == 0:
			return 'Hearts'
		elif self.suit == 1:
			return 'Spades'
		elif self.suit == 2:
			return 'clubs'
		elif self.suit == 3:
			return 'Diamonds'

#  2 3 4 5 6 7 8 9 10 j  q   k  a
#  0 1 2 3 4 5 6 7 8 9  10 11 12  13

	def get_rank(self):

		if self.rank < 8 :
			return str(self.rank + 2)
		elif self.rank == 9:
			return 'Jack'
		elif self.rank == 10:
			return 'Queen'
		elif self.rank == 11:
			return 'King'
		else:
			return 'Ace'

	def __str__(self):
		return self.get_rank() + ' of ' + self.get_suit()

	__repr__ = __str__

deck = []

for suit in range(4):
	for rank in range(13):
		deck.append(Card(suit, rank))

print(len(deck))

print(deck)



		