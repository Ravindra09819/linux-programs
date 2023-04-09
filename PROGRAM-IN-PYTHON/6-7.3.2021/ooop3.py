class C:
   def learnAndCode(self):
     print("Learning C Programming")


class Cpp:
   def learnAndCode(self):
     print("Learning C++ Programming")

class Golang:
   def learnAndCode(self):
     print("Learning Golang Programming")
class Demo:
     pass


class programmer:
   def Coding(self,language):
     language.learnAndCode()

cobj = C()
cpobj = Cpp()
gobj = Golang()
dobj = Demo()

obj = programmer()
obj.Coding(cobj)
obj.Coding(cpobj)
obj.Coding(gobj)
