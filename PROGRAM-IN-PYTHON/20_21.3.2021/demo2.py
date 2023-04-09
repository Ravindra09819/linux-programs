def main():

    name = input("Enter the file name that you want to creat")
    fobj =open(name,"w")
    str = input(" Enter the date that you want to write in the file  ")
    fobj.write(str)
if __name__ =="__main__":
    main()
