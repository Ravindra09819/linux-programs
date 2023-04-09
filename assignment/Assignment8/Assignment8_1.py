import threading
def evennum():
    i = 0
    cnt = 0
    print("First 10 even Number")
    while cnt<10:
        if i%2 == 0:
            print(i,end =" ")
            cnt+=1
        i+=1
def oddnum():
    i = 0
    cnt = 0
    print("First 10 even Number")
    while cnt<10:
        if i%2 != 0:
            print(i,end =" ")
            cnt+=1
        i+=1
def main():
    t1 = threading.Thread(target = evennum,args=())
    t2 = threading.Thread(target = oddnum,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ =="__main__":
    main()