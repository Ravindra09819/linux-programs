import multiprocessing
import os
def fun(number):
	print("pareant process of fun".os.getppid())
    print("process id of fun:",os getpid())
    for i in range(number)
        print(i)
def gun(number):
    print("pareant process of gun".os.getppid())
    print("process id of gun:",os getpid())
    for i in range(number)
        print(i)
if __name__ =="__main__":
    print("total cotes available",multiprocessing.cpu_count())
    print('parent process of main:', os.getppid())
    print('process id of main:', os.getpid())
    number = 3
    result = None
    p1 = multiprocessing.Process(target=fun, args=(number,))
    p2 = multiprocessing.Process(target=gun, args=(number,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
