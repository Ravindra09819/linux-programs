import os
import multiprocessing
def Process1(no):
    print("Process 1 is created")
    print("PID of process1 is ",os.getpid())
    print("PID of parent process1 is ",os.getppid())
    for i in range(no):
        print("process1:",i)
def Process2(no):
    print("Process 2 is created")
    print("PID of process2 is ",os.getpid())
    print("PID of parent process2 is ",os.getppid())
    for i in range(no):
        print("process2:",i)
def main():
    print("Inside main process")
    print("PID of main process is:",os.getpid())
    print("PID of parent process of main is:",os.getppid())
    value = 100
    p1 = multiprocessing.Process(target = Process1,args = (value,))
    p2 = multiprocessing.Process(target = Process2,args = (value,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("End of process")
if __name__ =="__main__":
    main()