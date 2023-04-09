x = input("How Many Number You Want In List \n")
arr=list()
for i in range(int(x)):
       no = input("Enter {} number \n".format(i))
      
       arr.append(int(no))
print("Element of List=",arr)
max = 0
for i in arr:
         if (i>max):
                  max = i

print("Maximum Number is=",max)