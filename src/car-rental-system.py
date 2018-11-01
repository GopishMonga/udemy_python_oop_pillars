# Class for Car rental system
class Rental:
	def __init__(self):
		self.available_cars = [{"name":"hatchback","rate":30},{"name":"sedan","rate":50},{"name":"suv","rate":100}]

	def display_available_cars(self):
		print()
		print("====>>>> Available Cars <<<<<====")
		for car in self.available_cars:
			print("Name: " + car["name"] + " Rate: " + str(car["rate"]))
		print()

	def calculate_rent(self,entered_car,days):
		print()
		print("====>>>> Price for Rent <<<<<====")
		print()
		print("You Entered below information")
		print("Name: " + entered_car + " Days: " + str(days))
		found = False
		for car in self.available_cars:
			if car["name"] == entered_car:
				found = True
				print("Car Found")
				result = car["rate"]*days
				print("Rent is ")
				print(result)
		
		if found is False:	
			print("Car not found")
		print()

# Class for user
class Customer:
	@staticmethod
	def input_info():
		print()
		car = input("Enter the name of car")
		days = input("Enter the days")
		return car + "*" + days


rental = Rental()
customer = Customer()


# Abstraction of System 
while True:
	print("Welcome to the car rental system")
	print("1. See Available Cars")
	print("2. Check Rental")
	print("3. Quit")
	user_input = int(input("Please enter your choice"))

	if user_input is 1:
		rental.display_available_cars()

	elif user_input is 2:
		user_selected = customer.input_info()
		info = user_selected.split("*")
		name = str(info[0])
		days = int(info[1])
		rental.calculate_rent(name,days)

	elif user_input is 3:
		quit()
	else:
		quit()

