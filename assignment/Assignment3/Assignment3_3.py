x = input("How Many Number You Want In List \n")
arr=list()
for i in range(int(x)):
       no = input()
       print(no,"is appended")
       arr.append(int(no))
print("Element of List=",arr)
min = 0
for i in arr:
       if (i <= min):
              min = i

print("Minimum Number is=",min)