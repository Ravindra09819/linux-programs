x = input("How Many Number You Want In List \n")
arr=list()
for i in range(int(x)):
       no = input()
      
       arr.append(int(no))
print("Element of List=",arr)
num = int(input("Element to search Number="))
cnt=0
for i in arr:
       if (i == int(num)):
              cnt = cnt+1

print("Number Found {} Times".format(cnt))