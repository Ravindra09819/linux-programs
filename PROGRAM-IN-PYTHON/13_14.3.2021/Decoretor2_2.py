def Substraction(no1,no2):
    print("2:Inside Substracton")
    return no1 - no2
def SubDecorator(fun_name):
    print("5:Inside SubDecorator")
    def Updator(a,b):
        print("7:Inside Updator")
        if a < b:
            a,b = b,a
        return fun_name(a,b)
    return Updator
def main():
    print("13:Inside main")
    Sub = SubDecorator(Substraction)
    print("Enter 1 Number=")
    value1 = int(input())
    print("Enter 2 Number=")
    value2 = int(input())
    ret = Sub(value1,value2)
    print("Substraction is ",ret)
    print("21:End of main")
if __name__ =="__main__":
    print("23:inside starter ")
    main()