import os
import time
def Square(no):
    return no * no
def SerialProcessing():
    start = time.time()
    print("SeriealProcessing")
    arr = range(100000)
    ret = []
    for i in arr:
        ret.append(Square(i))
    print("Result of serial processing:",ret)
    end = time.time()
    print(" time requred ",end-start)
def main():
    print("inside main")
    SerialProcessing()

if __name__ =="__main__":
    main()