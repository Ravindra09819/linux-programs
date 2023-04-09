x = input("How Many Number You Want In List \n")
arr=list()
for i in range(int(x)):
       no = input()
       print(no,"is appended")
       arr.append(int(no))
print("Element of List=",arr)
sum = 0
for i in arr:
         sum = sum + i
print("Addition of Number in List is=",sum)