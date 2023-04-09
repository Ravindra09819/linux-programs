from functools import reduce

x=input("How many numbers you want in list \n")

arr=list()

for i in range(int(x)):
	no=input("Enter {} number\n".format(i))
	print(no," is appended\n")
	arr.append(int(no))
print("Elements of list :- ",arr)

Filter_arr=list(filter(lambda no:(70<=no<=90) ,arr ))
print("Filtered List",Filter_arr)

Map_arr=list(map(lambda no:no+10,Filter_arr))
print("Mapped List",Map_arr)

ans=reduce(lambda no1,no2:no1*no2,Map_arr)

print("Reduced answer",ans)