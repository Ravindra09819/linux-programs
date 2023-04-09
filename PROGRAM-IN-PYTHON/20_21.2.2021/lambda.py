def Addition(no1,no2):
     return no1 + no2

 
sum = lambda no1,no2:no1 + no2

def fun(name):
    ret = name(10,20)
    print("Value from fun :",ret)

def main():
    print("Enter First Number:")
    value1 = int(input())
    print("Enter second Number:")
    value2 = int(input())
    ret = Addition(value1,value2)
    print("Addition is ",ret)
    ret = sum(value1,value2)
    print("Addition with lambda is :",ret)
    fun(sum)

if __name__=="__main__":
   main()









