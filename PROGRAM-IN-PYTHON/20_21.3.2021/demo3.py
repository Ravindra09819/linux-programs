def main():

    name = input("Enter the file name that you want to creat")
    fobj =open(name,"r")
    
    
    print("date from is:")
    for Date in fobj:
        print(Date,end="")
if __name__ =="__main__":
    main()
