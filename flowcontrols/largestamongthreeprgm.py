num1=int(input("enter the value for num1"))
num2=int(input("enter the value for num2"))
num3=int(input("enter the value for num3"))
if((num1>num2)&(num1>num3)):
    print("num1 is max")

if((num2>num3)):
    print("num2 is second largest")
    print("orde is",num1,num2,num3)
elif((num2>num1)&(num2>num3)):
    print("num2 is max")
if((num1>num3)):
    print("num1 is second largest")
    print("order is",num2,num1,num3)
elif((num3>num1)&(num3>num2)):
    print("num3 is max")
if((num1>num2)):
    print("num1 is second largest")
else:
    print("num2 is second largest")
    print("order is",num3,num1,num2)
