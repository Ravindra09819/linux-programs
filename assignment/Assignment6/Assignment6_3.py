class Arithmetic():
     def __init__(self):
            self.value1 = 0
            self.value2 = 0
     def accept(self):
            self.value1 = int(input("Enter First Number \n : "))
            self.value2 = int(input("Enter Second Number \n: "))

     def Addition(self):
            return(self.value1 + self.value2) 

     def Substraction(self):
            return(self.value1 - self.value2) 

     def Multiplication(self):
            return(self.value1 * self.value2) 

     def Division(self):
            return(self.value1 / self.value2) 
 
obj = Arithmetic()
obj.accept()
print(obj.Addition())
print(obj.Substraction())
print(obj.Multiplication())
print(obj.Division())

