def Substraction(no1,no2):
    return no1 - no2
def SubDecorator(fun_name):
    def Updator(a,b):
        if a < b:
            a,b = b,a
        return fun_name(a,b)
    return Updator


def main():
    Sub = SubDecorator(Substraction)
    print("Enter 1 Number=")
    value1 = int(input())
    
    print("Enter 2 Number=")
    value2 = int(input())
    ret = Sub(value1,value2)

    print("Substraction is ",ret)
if __name__ =="__main__":
    main()