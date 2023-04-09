
class Numbers:
     
     def __init__(self,no):
         self.size = no
         self.arr = []

     def __del__(self):
         print(" Dealocting the memory of object  ")
         del self.arr

     def Accept(self):
         print("Please Enter the elemrnt")
         for i in range(self.size):
             print("Enter Number:",i + 1)
             self.arr.append(int(input()))

     def Display(self):
         print("Element of List are")
         for i in range(self.size):
             print(self.arr[i]) 
   
     def Summation(self):
         sum = 0
         for i in range(self.size):
              sum = sum + self.arr[i]
         return sum

     def EvenDisplay(self):
         print("Even element from list are=")
         for i in range(self.size):
             if (self.arr[i] % 2) == 0:
                 print(self.arr[i])

     def perfectDisplay(self):
         sum = 0
         for i in range(self.size):
             for j in range(1,int(self.arr[i]/2)+1):
                 if(self.arr[i] % j) == 0: 
                    sum = sum + j
             if sum == self.arr[i]:
                 print(self.arr[i])
             sum = 0             

     def primeDisplay(self):
         Flag = False
         for i in range(self.size):
             for j in range(2,int(self.arr[i]/2)+1):
                 if(self.arr[i] % j) == 0: 
                    Flag = True
                    break
                 if Flag == False:
                     print(self.arr[i])
                 Flag = False
                        
def main():
    print("Enter Number fo Element")
    value = int(input())

    obj1 = Numbers(value)
    obj1.Accept()
    obj1.Display()

    ret = obj1.Summation()
    print("Summation of all element:",ret)

    obj1.EvenDisplay()

    print("perfect number are=")
    obj1.perfectDisplay()

    print("prime number are=")
    obj1.primeDisplay()
    del obj1
  
if __name__ =="__main__":
   main() 