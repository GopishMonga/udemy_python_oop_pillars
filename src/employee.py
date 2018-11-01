class Employee:
	first_name = "Gopu"
	last_name = "Monga"
	def change_name(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	@staticmethod
	def print_hello():
		print("Hello World!")


employee_first = Employee()
print(employee_first.first_name + " " + employee_first.last_name)
employee_first.change_name("Gops","Mongu")
print(employee_first.first_name + " " + employee_first.last_name)
employee_first.print_hello()