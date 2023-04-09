number = int(input("Enter Any Number:"))
if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
             print(number,"Is Not Prime Number")
             break
        else:
            print(number,"Is Prime Number")
else:
    print(number,"Is Not Prime Number")
