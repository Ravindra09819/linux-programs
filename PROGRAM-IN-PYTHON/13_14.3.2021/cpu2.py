import os
import time
import multiprocessing
def Square(no):
    return no * no

def parallelProcessing():
    start = time.time()
    print("parallelProcessing")
    arr = range(10000)
    ret = []
    pobj = multiprocessing.Pool()
    ret = pobj.map(Square,arr)
    end = time.time()
    print(" time requred ",end-start)

def SerialProcessing():
    start = time.time()
    print("SeriealProcessing")
    arr = range(10000)
    ret = []
    for i in arr:
        ret.append(Square(i))
    end = time.time()
    print(" time requred ",end-start)

def main():
    print("inside main")
    SerialProcessing()
    parallelProcessing()

if __name__ =="__main__":
    main()