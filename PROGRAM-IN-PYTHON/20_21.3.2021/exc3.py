
def main():
    no1 = int(input("Enter 1 number"))
    no2 = int(input("Enter 2 number"))
    try:
        print("inside try")
        ans = no1 / no2
    except ZeroDivisionError as obj:
        print("Divide by zero excetion",obj)
    else:
        print("Division is ",ans)
    finally:
        print("inside finally")
        print("Deallocate all the resurce")

if __name__ =="__main__":
    main()
