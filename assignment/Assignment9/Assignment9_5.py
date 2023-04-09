from collections import Counter


string=input("Enter string \n")
name=input("Enter name of file\n")

fp=open(name,"r")
r=fp.read().lower()
print("Number of words in the file :",r.count(string.lower()))