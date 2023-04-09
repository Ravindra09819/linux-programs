import threading
def evenlist(list):
    sum=0
    for i in list:
        if i%2==0:
            sum+=i
    print(sum)
def oddlist(list):
    sum=0
    for i in list:
        if i%2!=0:
            sum+=i
    print(sum)
def main():
    arr = [22,25,10,12,45,44,87,76,87,45,87,35,30]
    Thread1 = threading.Thread(target = evenlist,args=(arr,())
    Thread2 = threading.Thread(target = oddlist,args=(arr,())
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()
if __name__=="__main__":
    main()