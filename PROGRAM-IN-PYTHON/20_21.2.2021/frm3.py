def checkeven(no):
     if (no % 2) == 0:
         return True
     else:
         return False 


def Increment(no):
    return no +2
 
def add(x,y):
    return x +y




def main():
    arr = []
    print("Enter number of element ")
    size = int(input())
    
    for i in range(size):
         print("enter element no:",i+1)
         no = int(input())
         arr.append(no)
    print("you enter data:",arr)
    newdata = filter(checkeven,arr)
    print("after filter data :", newdata)

if __name__ ==" __main__":
    main()