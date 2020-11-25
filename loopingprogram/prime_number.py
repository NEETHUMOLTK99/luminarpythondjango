num=int(input("enter the number"))
flg=0
for i in range(2,num):
    if(num%i==0):
        flg+=1
        break
        if(flg==0):
            print("prime number")
else:
    print("not a prime number")