class Gem:
	# Define Properties of Class Gem
	count_of_gems = 0
	iterator_of_gems = 1
	array_of_gems = []

	# Define Constructor of Class Gem
	def __init__(self):
		print("START of INIT Constructor")
		# if numbers of gems are 5, then delete first and store new
		if Gem.count_of_gems == 5:
			print("Count of Gems is equal to 5")
			Gem.array_of_gems.pop(0)

		elif Gem.count_of_gems < 5:
			print("Count of Gems is less than 5")
			Gem.count_of_gems += 1

		elif Gem.count_of_gems > 5:
			print("Count of Gems is less than 5")
			return

		print("Creating new Gem")
		self.gem_id = Gem.iterator_of_gems
		print("New Gem Created with ID: "+ str(self.gem_id))
		Gem.iterator_of_gems += 1
		print("Iterator of Gems is incremented to "+ str(Gem.iterator_of_gems))
		Gem.array_of_gems.append(self.gem_id)
		print("==== Now the array of gems looks like ====")
		print(Gem.array_of_gems)
		print("==== END of INIT Constructor")
		
gem1 = Gem()
gem2 = Gem()
gem3 = Gem()
gem4 = Gem()
gem5 = Gem()
gem6 = Gem()
gem7 = Gem()


