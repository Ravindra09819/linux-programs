
def main():
    arr = {10,20.5,"hellow",120}
    print(type(arr))
    print(arr)
    print(len(arr))
    for value in arr:
        print(arr)
    if "hellow" in arr:
        print("helow")
    arr.remove(120)
    print(arr)
    arr.add(20)
    print(arr)
    arr.discard(120)
    print(arr)
        
if __name__ =="__main__":
	main()