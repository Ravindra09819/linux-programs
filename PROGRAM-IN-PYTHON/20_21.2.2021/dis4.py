def check(name):
    try :
        fd = open(name,"r")
        print("File found in current directory")
    except FileNot rror as e:
        print("Error is :",e)
    finally:
        print("Successfully done")
def main():
    x= input("Enter Name of the File \n")
    check(x)
if __name__ =="__main__":
    main()