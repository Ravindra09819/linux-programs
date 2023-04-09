class Base:
   def __init__(self):
      self.i =10
      self.j =20
      print("Inside Base Construction")
   
   def fun(self):
      print("Inside Base Fun")

   def gun(self):
      print("Inside Base gun")
class Derive(Base):
   def __init__(self):
      Base.__init__(self)
      self.x = 30
      self.y = 40
      print("Inside derive constructor")
   def sun(self):
      print("Inside Derive sun")
   def gun(self):
      print("Inside Derive gun")

def main():
   bobj = Base()
   print(bobj.i)
   print(bobj.j)
   bobj.fun()
   bobj.gun() 
   dobj = Derive()
   print(dobj.i)
   print(dobj.j)
   print(dobj.x)
   print(dobj.y)
   dobj.sun()
   dobj.gun()
   dobj.fun()
    
if __name__ == "__main__":
    main()