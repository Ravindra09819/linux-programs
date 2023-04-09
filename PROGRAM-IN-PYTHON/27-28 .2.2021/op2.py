def Add(no1,no2):
    return no1+no2

def Sub(no1,no2):
    return no1-no2

def main():
    value1 = (int(input("Enter First Number:")))

    Value2 = (int(input("Enter Second Number:")))

    
    ret = Add(value1,Value2)
    print("Addition=",ret)

    ret = Sub(value1,Value2)
    print("Substraction=",ret)

if __name__ =="__main__":
   main()