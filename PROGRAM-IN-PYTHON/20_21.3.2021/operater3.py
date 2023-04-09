class Student:
    def __init__(self,str,a,b,c):
        self.name = str
        self.m1 = a
        self.m2 = b
        self.m3 = c
    def __eq__(self,other):
        return((self.m1==other.m1) and (self.m2==other.m2) and (self.m3==other.m3))

    def __gt__(self,other):
        return((self.m1>other.m1) and (self.m2>other.m2) and (self.m3>other.m3))


def main():
    obj1 =Student("Aniket",99,89,99)
    obj2 =Student("sachin",88,87,99)
    if obj1 == obj2:
        print("Both the student are same")
    else:
        print("Both the student are different")
        
    if obj1>obj2:
        print("first object is gerater")
    else:
        print("second object is gerater")
if __name__ =="__main__":
    main()