class Numbers:
	def __init__(self,value):
		self.value=value;

	def chkprime(self):
		for i in range(2,int(self.value/2)):
			if(self.value%i==0):
				return False
		return True

	def chkperfect(self):
		sum=self.Sumfactors()
		if(sum==self.value):
			return True
		else:
			return False

	def Factors(self):
		print("Factors :-")
		for i in range(1,self.value):
			if(self.value%i==0):
				print(i,end=' ')

		print("\n")

	def Sumfactors(self):
		sum=0
		for i in range(1,self.value-1):
			if(self.value%i==0):
				sum=sum+i
		return sum

x=int(input("Enter a number \n"))
obj1=Numbers(x)
if obj1.chkprime():
	print(x," is prime")
else:
	print(x," is Not prime")
obj1.Factors()
print(obj1.Sumfactors())
if obj1.chkperfect():
	print(x ," is a perfect number")
else:
	print(x ," is Not a perfect number")