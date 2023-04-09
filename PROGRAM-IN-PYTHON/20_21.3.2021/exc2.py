
def main():
    no1 = int(input("Enter 1 number"))
    no2 = int(input("Enter 2 number"))
    try:
        ans = no1 / no2
    except ZeroDivisionError as obj:
        print("Divide by zero excetion",obj)
    except Exception as eobj:
        print("Exception occure",eobj)
    else:
        print("Division is ",ans)

if __name__ =="__main__":
    main()
