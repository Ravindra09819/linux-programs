
def fun():
      for i in range (row,0,-1):
         return i
         fun()

def main():
    row = int(input("\n Enter no ="))
    for i in range (row,0,-1):
        print(i,end=" ")
       
if __name__ =="__main__":
    main()