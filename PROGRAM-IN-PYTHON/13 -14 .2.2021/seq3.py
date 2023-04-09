def checkeven(no):
    if no % 2 == 0:
      return true
    else:
       return folse


def main():
    print("enter number:")
    value = int(input())

    bret = checkeven(value)

    if bret == true:
       print("{}is even number ".formate(value))
    else:
       print("{}is odd number ".formate(value))

if __name__=="__main__":
    main()