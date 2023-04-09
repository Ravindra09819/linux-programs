import MarvellousNum

x = input("How Many Number You Want In List \n")
arr=list()
for i in range(int(x)):
       no = input()
       print(no,"is appended")
       arr.append(int(no))
print("Element of List=",arr)

def ListPrime(arr):
     sum = 0
     for i in arr:
        x = MarvellousNum.ChkPrime(i)
        if (x == i):
                   print(i,end=" ")
                   sum =sum +i
        return sum
ans = ListPrime(arr)

print("Addition of Prime Number is=",ans)