class Arithematic:
    def __init__(self,i,j):
       print("Inside Constructor")
       self.no1 = i
       self.no2 = j

    def Add(self):
        return self.no1 + self.no2

    def Sub(self):
        return self.no1 - self.no2

def main():
    obj1 = Arithematic(21,11)
    obj2 = Arithematic(101,51)
    
    ret = obj1.Add()
    print("Addition=",ret)
    ret = obj1.Sub()
    print("Substration=",ret)


    ret = obj2.Add()
    print("Addition=",ret)
    ret = obj2.Sub()
    print("Substration=",ret)
    
    
    
    

if __name__ =="__main__":
   main()