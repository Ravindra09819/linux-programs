def Addition(LIST):
    sum = 0
    for i in range(len(LIST)):
       sum = sum + LIST[i]
    return sum

def main():
    arr = []
    print("Enter number of element")
    size = int(input())
   
    for i in range(size):
       print("Enter element no:",i + 1)
       value = int(input())
       arr.append(value)
    print("Accepted date is :",arr)
    ret = Addition(arr)
    print("Addition of all element ",ret)

if __name__ == "__main__":
     main()