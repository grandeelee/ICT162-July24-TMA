class Card:
	def __init__(self, number, balance):
		self._number = number
		self._balance = balance

class Bank:
	def __init__(self):
		self._cards = []

	def addCard(self, card):
		if card not in self._cards:
			self._cards.append(card)
		else:
			raise Exception("card exist")

if __name__ == "__main__":
	b1 = Bank()
	c1 = Card("123", 100)
	c2 = Card("123", 100)
	c3 = Card("123", 100)
	b1.addCard(c1)
	b1.addCard(c2)
	b1.addCard(c3)

	print(b1._cards)