def Substraction(no1,no2):
    return no1 - no2
def SubDecorator(fun_name):
    return fun_name(10,5)

def main():

    ret = SubDecorator(Substraction)
    print("Substraction is ",ret)
if __name__ =="__main__":
    main()