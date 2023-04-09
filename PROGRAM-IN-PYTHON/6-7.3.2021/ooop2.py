class Base:
   def __init__(self):
       self.i = 10
       self.j = 20

   def fun(self):
       print("Base fun")
class Derive(Base):
   def __init__(self):
      Base.__init__(self)
      self.x = 30
      self.y = 40
   def gun(self):
      print("Derive gun")
      Base.fun(self)
      self.fun()
      super().fun()
 
      print(self.i)
      
dobj = Derive()
dobj.gun()
