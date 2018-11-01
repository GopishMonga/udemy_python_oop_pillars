from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
	@abstractmethod
	def createAccount():
		return 0
	@abstractmethod
	def authenticate():
		return 0
	@abstractmethod
	def deposit():
		return 0
	@abstractmethod
	def withdraw():
		return 0
	@abstractmethod
	def displayBalance():
		return 0

class SavingsAccount(Account):
	def __init__(self):
		self.savingsAccounts = {}

	def createAccount(self,name,initial_deposit):
		print()
		self.accountNumber = randint(10000,99999)
		self.savingsAccounts[self.accountNumber] = [name,initial_deposit]
		print("Account Created Successfully. Your account number is {}".format(self.accountNumber))
		print()

	def authenticate(self,name,account_number):
		print()
		if account_number in self.savingsAccounts.keys():
			if name == self.savingsAccounts[account_number][0]:
				print("Authentication Successful!")
				self.accountNumber = account_number
				return True
			else:
				print("Authentication Failed! Name doesn't match records")
				return False
		else:
			print("Authentication Failed! Account Number doesn't exist. ")
			return False

	def deposit(self,deposit_amount):
		print()
		self.savingsAccounts[self.accountNumber][1] += deposit_amount
		print("Deposit Successful!")
		self.displayBalance()
		print()

	def withdraw(self,withdraw_amount):
		print()
		if self.savingsAccounts[self.accountNumber][1] < withdraw_amount: 
			print("Insuffiencent Funds!")
			self.displayBalance()
			print()
			return False
		else: 
			self.savingsAccounts[self.accountNumber][1] -= withdraw_amount
			print("Withdraw Successful!")
			self.displayBalance()
			print()
			return True

	def displayBalance(self):
		print()
		print("Available Balance is {}".format(self.savingsAccounts[self.accountNumber][1]))


savingsAccount = SavingsAccount()
while True:
	print()
	print("Welcome to Monga Bank. Select a number from below")
	print("1. Create New Account")
	print("2. Existing Account")
	print("3. Quit")
	user_input = int(input("Input a number to proceed."))

	if user_input is 1:
		print("You have selected to create new account")
		name = input("Please enter your name")
		initial_deposit = int(input("Please enter your initial_deposit"))
		print()
		savingsAccount.createAccount(name,initial_deposit)

	elif user_input is 2:
		print("You have selected existing acount")
		name = input("Please enter your name")
		account_number = int(input("Please enter your account number"))
		isAuthenticated = savingsAccount.authenticate(name,account_number)
		if isAuthenticated is True:
			while True:
				print()
				print("Welcome {}".format(savingsAccount.savingsAccounts[savingsAccount.accountNumber][0]))
				print("1. Check Balance")
				print("2. Withdraw")
				print("3. Deposit")
				print("4. Go Back to Previous Menu")
				user_choice = int(input("Enter your choice"))
				if user_choice is 1:
					savingsAccount.displayBalance()
				elif user_choice is 2:
					withdraw_amount = int(input("Please enter withdrawal amount"))
					savingsAccount.withdraw(withdraw_amount)
				elif user_choice is 3:
					deposit_amount = int(input("Please enter deposit amount"))
					savingsAccount.deposit(deposit_amount)
				elif user_choice is 4: 
					break

	elif user_input is 3:
		quit()		


