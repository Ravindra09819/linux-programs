
def summation(n):
    summation = 0
    for digit in str(n):
         summation += int(digit)
    return summation
    summation(n)

def main():
    n = (int(input("Enter The Number:")))
    print(summation(n))

if __name__ =="__main__":
   main()