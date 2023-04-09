import os

def main():
    print("inside main")
    print("numner of CPU cores:",os.cpu_count())

if __name__ =="__main__":
    main()