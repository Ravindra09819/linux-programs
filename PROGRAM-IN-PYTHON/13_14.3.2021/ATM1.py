import threading
Amount = 1000

def ATM(func):
    func()
def Deposir():
    value = int(input("Enter the amount to deposit"))
    global Amount
    Amount = Amount + value
    print("Deposit succesful - Balance:",Amount)
def Withdraw():
    value = int(input("Enter the amount to withdraw"))
    global Amount
    if value > Amount:
        print("there is no suffceient Balance")
    else:
        Amount = Amount - value
        print("Withdraw succesful - Balance:",Amount)
def main():
    ATM(Deposir)
    ATM(Withdraw)

if __name__ == "__main__":
    main()