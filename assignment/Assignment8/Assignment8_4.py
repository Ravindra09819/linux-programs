import threading
def Small_let(name):
    print(threading.current_thread().name)
    print(threading.get_ident())
    for i in name:
        if(i<='a' and i<='z'):
            print(i,"is small")
def Capital_let(name):
    print(threading.current_thread().name)
    print(threading.get_ident())
    for i in name:
        if(i<='A' and i<='Z'):
            print(i,"is Capital")
def Digit(name):
    print(threading.current_thread().name)
    print(threading.get_ident())
    for i in name:
        if i is digit():
            print(i,"is Digit")
def main():
    name = input("enter name \n")
    small = threading.Thread(target=Small_let,args=(name,))
    capital = threading.Thread(target=Capital_let,args=(name,))
    digit = threading.Thread(target=Digit,args=(name,))
    small.start()
    small.join()
    capital.start()
    capital.join()
    digit.start()
    digit.join()
if __name__=="__main__":
    main()