import Arithmetic
def main():
    n1 = int(input("Enter The First Number="))
    n2 = int(input("Enter The Second Number="))
    ans1 = Arithmetic.Add(n1,n2)
    print("Addition:",ans1)
    ans2 = Arithmetic.Sub(n1,n2)
    print("Substraction:",ans2)
    ans3 = Arithmetic.Mul(n1,n2)
    print("Multipliction:",ans3)
    ans4 = Arithmetic.Div(n1,n2)
    print("Division:",ans4)
if __name__ =="__main__":
    main()