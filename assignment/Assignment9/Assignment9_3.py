import sys

x = sys.argv[1]

fd=open("Demo1.txt","x")
fp=open(x,"r")

fd.write(fp.read())

fd.close()
fp.close()

fd1=open("Demo.txt","r")
print("Information about file",fd1)
print(fd1.read())