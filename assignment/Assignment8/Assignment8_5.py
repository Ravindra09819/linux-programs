import threading

def fun():
	for i in range(1,51):
		print(i)

def gun():
	for i in range(50,0,-1):
		print(i)

thread1=threading.Thread(target=fun,args=())
thread2=threading.Thread(target=gun,args=())

thread1.start()
thread1.join()

thread2.start()

thread2.join()