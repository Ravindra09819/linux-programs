def factor(x):
    print("The Factor of ",x,"arc:")
    for i in range(1,x+1):
        if x % i == 0: 
               print(i)
num = (int(input("Enter Number:")))
factor(num)