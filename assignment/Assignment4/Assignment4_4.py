from functools import reduce

x=input("How many numbers you want in list \n")

arr=list()

for i in range(int(x)):
	no=input("Enter {} number\n".format(i))
	print(no," is appended\n")
	arr.append(int(no))

print("Elements of list :- ",arr)

Filter_arr=list(filter(lambda no:(no%2==0),arr))
print("Filtered List => ",Filter_arr,end="\n\n")

Map_arr=list(map(lambda no:no*no,Filter_arr))
print("Mapped List => ",Map_arr,end="\n\n")

Ans=reduce(lambda no1,no2:no1+no2,Map_arr)
print("Reduced answer => ",Ans,end="\n\n")