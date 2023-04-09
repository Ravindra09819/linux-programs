def fun():
    print("inside fun")




def gun(value):
    print("insidegun",value)

def sun(value):
    value=value+1
    print("inside sun")
    return value
def mun():
    pass

def Outer():
    print("Inside Outer")
    def inner():
        print("Inside inner")

def main():

    fun()
    gun(11)
    ret=sun(10)
    print(ret)
    mun()
    Outer()
if __name__=="__main__":
    main()