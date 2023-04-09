import functools

checkeven = lambda no:(no % 2)
Increment = lambda no:no +2
add = lambda x,y: x +y
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