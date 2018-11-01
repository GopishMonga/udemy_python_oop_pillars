class Square:
	def __init__(self,side):
		self.side = side
	def __pow__(square1,square2):
		return square1.side ** square2.side

square1 = Square(3)
square2 = Square(4)
result = square1 ** square2
print("Result is " + str(result))