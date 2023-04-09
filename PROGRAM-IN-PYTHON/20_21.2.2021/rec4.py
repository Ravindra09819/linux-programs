import sys



def main():
     print("Recurion limit :",sys.getrecursionlimit())
   
     sys.setrecursionlimit(1500)
     print("Recurion limit :",sys.getrecursionlimit())

if __name__== "__main__":
    main()