from functools import reduce

x=input("How many numbers you want in list \n")

arr=list()

for i in range(int(x)):
	no=input("Enter {} number\n".format(i))
	print(no," is appended\n")
	arr.append(int(no))


print("Elements of list :- ",arr)


def chkprime(no):
	for i in range(2,int(no/2)):
		if(no%i==0):
			return 0

	return 1

Filter_arr=list(filter(chkprime,arr))
print("Filtered List => ",Filter_arr,end="\n\n")


Mapped_Arr=list(map(lambda no:no*2,Filter_arr))
print("Mapped List => ",Mapped_Arr,end="\n\n")

answer=reduce(lambda x,y: x if (x>y) else y , Mapped_Arr)
print("Reduced answer => ",answer,end="\n\n")