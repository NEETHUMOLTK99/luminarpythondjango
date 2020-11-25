low_limit=int(input("enter the lower limit"))
up_limit=int(input("enter the upper limit"))
sum=0
while(low_limit<=up_limit):

    if(low_limit%2==0):
        sum=sum+low_limit
        print(low_limit)
        low_limit+=1
        print("sum of even number")
else:
    print("sum of odd numbers")