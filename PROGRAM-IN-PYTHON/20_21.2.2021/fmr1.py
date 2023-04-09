def cheakeven(no):
      if no % 2 == 0:
         return True
      else:
         return False

def marv(arr):
      brr = []
      for i in range(len(arr)):
          if cheakeven(arr[i]) == True:
             brr.append(arr[i])
      return brr
    

def main():
    arr = []
    print("Enter number of element ")
    size = int(input())
    
    for i in range(size):
         print("enter element no:",i+1)
         no = int(input())
         arr.append(no)
    print("you enter data:",arr)
    newdata = marv(arr)
    print("after filter data :", newdata)



if __name__=="__main__":
     main()