import threading
def evenfactor(number):
    i=0
    sum = 0
    for i in range(1,number):
        if (number%i==0):
            if i%2==0:
                print(i,end=" ")
                sum = sum +i
    print("Sum of Even factors",sum)
def oddfactor(number):
    sum = 0
    for i in range(1,number):
        if (number%i==0):
            if i%2!=0:
                print(i,end=" ")
                sum = sum +i
    print("Sum of Odd factors",sum)
def main():
    number = 20
    t1 = threading.Thread(target = evenfactor,args =(number,))
    t2 = threading.Thread(target = oddfactor,args =(number,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Exist for main")
if __name__ =="__main__":
    main()