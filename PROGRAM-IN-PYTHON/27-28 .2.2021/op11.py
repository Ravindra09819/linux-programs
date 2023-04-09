class Demo:
    x = 10
    y = 20

    def __init__(self):
        print("Inside Constructor")
        self.i = 30
        self.j = 40
     
    def __del__(self):
        print("Inside destructor")
     
    def fun(self):
        print("Inside fun")

def main():
    obj1 = Demo()
    obj2 = Demo()
    
    obj1.fun()
    obj2.fun()
    del obj1
    del obj2
    
   


if __name__ =="__main__":
   main()