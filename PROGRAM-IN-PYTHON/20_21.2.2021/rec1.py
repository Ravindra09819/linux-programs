
def DisplayI(no):
     for i in range(no):
          print("Hello")

def DisplayIW(no):
    while no != 0:
        print("Hello")
        no = no - 1
 
def DisplayR(no):
     if no != 0:
           no = no - 1
           print("Hello")
           DisplayR(no)



def main():

    print("Enter the number of itration")
    value = int(input())

    print("Calling iterative function with for loop")
    DisplayI(value)
  
    print("Calling iterative function with while loop")
    DisplayIW(value)

    print("Calling the recursive function")
    DisplayR(value)

if __name__== "__main__":
    main()