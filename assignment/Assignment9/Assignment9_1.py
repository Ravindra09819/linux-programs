def check(name):
    try:
        fd = open(name,"r")
        print("File found in current directory")
    except FileNotFoundError as e:
        print("Error is :",e)
    finally:
        print("Successfully done")
x = input("Enter Name of the File \n")
check(x)
