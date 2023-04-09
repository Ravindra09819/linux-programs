import threading
Amount = 1000

def ATM(func,kulup):
    func(kulup)
    
def Deposit(kulup):
    kulup.acquire()
    value = int(input("Enter the amount to deposit"))
    global Amount
    Amount = Amount + value
    print("Deposit succesful - Balance:",Amount)
    kulup.release()
    
def Withdraw(kulup):
    kulup.acquire()
    value = int(input("Enter the amount to withdraw"))
    global Amount
    if value > Amount:
        print("there is no suffceient Balance")
    else:
        Amount = Amount - value
        print("Withdraw succesful - Balance:",Amount)
    kulup.release()

def main():
    print("inside main")
    
    kulup = threading.Lock()
    t1 = threading.Thread(target = ATM,args = (Deposit,kulup))
    t2 = threading.Thread(target = ATM,args = (Withdraw,kulup))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("ATM Appliction closed")

if __name__ == "__main__":
    main()