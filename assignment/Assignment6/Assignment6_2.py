class Circle:
      PI = 3.14
      def __init__(self):
            self.red = 0.0
            self.area = 0.0
            self.circum = 0.0
    
      def accept(self):
	      x = (float(input("Enter the value of radius \n")))
	      self.rad = x

      def calculateArea(self):
	      a= (self.PI * self.rad * self.rad)
	      self.area=a

      def circumference(self):
	      circumf=2 * self.PI * self.rad
	      self.circum=circumf

      def display(self):
	      print(self.rad)
	      print(self.area)
	      print(self.circum)

obj1=Circle()
obj1.accept()
obj1.calculateArea()
obj1.circumference()
obj1.display()

obj2=Circle()
obj2.accept()
obj2.calculateArea()
obj2.circumference()
obj2.display()

obj3=Circle()
obj3.accept()
obj3.calculateArea()
obj3.circumference()
obj3.display()
