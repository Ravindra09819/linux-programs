def Additionf(data):
     sum = 0
     for i in range(len(data)): sum = sum + data[i]
     return sum

def Additionw(data):
     sum = 0
     i =0 
     
     while i < len(data): 
      sum = sum + data[i]
      i = i + 1
     return sum


sum = 0
i = 0
def Additionr(data):
    global sum
    global i
    if i < len(data):
      sum = sum + data[i]
      i = i + 1
      Additionr(data)
    return sum

      

def main():
   arr =[]
   size = int(input("Enter the size of array"))
   for i in range(size): arr.append(int(input()))
   print("Date is:",arr)
   
   print("Addition is ",Additionf(arr))   

   print("Addition is ",Additionw(arr))   

   print("Addition is ",Additionr(arr))   

if __name__== "__main__":
    main()