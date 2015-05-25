class Customer(object):
	"""A customer of WRC Bank with a checking account. Customers have
	the following properties:

	Attributes:
		name: A string representation of the customer's name.
		balance: A float tracing the current balance of the customer's account.
	"""

	def __init__(self, name, balance=0.0):
		"""Return a customer object whose name is *name* and starting
		balance is *balance*."""
		self.name = name
		self.balance = balance

	def withdraw(self, amount):
		"""Return the balance remaning after withdrawing *amount*
		dollars."""
		if amount > self.balance:
			raise RuntimeError('AMount great than available balance.')
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		"""Returns the balance remaining after depositing *amount*
		dollars."""
		self.balance += amount
		return self.balance