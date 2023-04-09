import sys

x=sys.argv[1]
y=sys.argv[2]

fp=open(x,"r")
fp1=open(y,"r")


if (fp.read()==fp1.read()):
    print("Content of both files are same")
else:
    print("Both files cotains Different contents")