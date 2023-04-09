def factorial(n):
    if n == 0:
       return 1
    else :
       return n * factorial(n-1)
       factorial(n)
def main():
       n = (int(input("Enter The Number :")))
       print(factorial(n))
if __name__ =="__main__":
   main()