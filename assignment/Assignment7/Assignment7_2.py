class BankAccount:
	ROI = 10.5
	def __init__(self,Name,amt):
		self.name = Name
		self.amount = amt

	def Display(self):
		print("Name=",self.name)
		print("Amount=",self.amount)

	def Deposit(self,amt):
		self.amount -= amt
		print("After Depositing = ",self.amount)

	def Withdraw(self,amt):
		print("After Withdraw = ",self.amount)

	def Calculate(self):
		intrest = ((self.ROI)*(self.amount))/100
		print("Rate of interet =",intrest)

obj1 = BankAccount("sachin",15000)
obj1.Display()
obj1.Calculate()
obj1.Deposit(1000)
obj1.Withdraw(3400)
obj1.Display()
print("\n")
obj2 = BankAccount("navnath",100000)
obj2.Display()
obj2.Calculate()
obj2.Deposit(10000)
obj2.Withdraw(20000)
obj2.Display()
