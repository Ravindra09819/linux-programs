class marvellous:
   value1 = 11
   def __inif__(self,no1,no2):
      self.i = no1
      self.j = no2
      print("Inside Constructor")
   def __del__(self):
      print("Inside destructor") 
   def fun(self):
      print("inside fun method") 
      print("value of j is ",self.j)
def main():
   obj1 = marvellous(11,21)
   obj2 = marvellous(51,101)
   print("value of i fron obj1",obj1.i)
   print("value of i fron obj2",obj2.i)
   print("value of class member",marvellous.value1)
   obj1.fun()
   obj2.fun()
   del obj1
   del obj2
if __name__ == "__main__":
   main()