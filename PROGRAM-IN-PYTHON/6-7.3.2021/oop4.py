class Base:
   def __init__(self):
      self.i =10
      self.j =20
      print("Inside Base Construction")
class Derive1(Base):
   def __init__(self):
      Base.__init__(self)
      self.x = 30
      self.y = 40
      print("Inside derive1 constructor")
class Derive2(Base):
   def __init__(self):
      Derived1.__init__(self)
      self.a = 50
      self.b = 60
      print("Inside derive2 constructor")


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