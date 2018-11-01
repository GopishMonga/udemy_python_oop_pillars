class Honda:
	corporation = "Honda Inc."
	def display(self):
		print("Corporation is {} & Model is {}".format(self.corporation,self.model))

class City(Honda):
	def __init__(self):
		self.model = "City 2018"

city = City()
city.display()

