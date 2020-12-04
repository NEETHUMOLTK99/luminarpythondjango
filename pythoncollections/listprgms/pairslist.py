lst=[1,2,3,4,5,6,7,8]
element=int(input("enter the element"))
flg=0
for num in lst:
    if(element==num):
        flg=+1
        break
    else:
        flg=0
    if(flg==0):
        print("element not found")
    else:
        print("element found")







lst=[1,2,3,4,6]

low=0
upp=len(lst)-1

element=7
while(low<upp):
    total=lst[low]+lst[upp]
    if(element<total):
        upp=upp-1
    elif(element>total):
        low=low+1
    elif(element==total):
        print(lst[low],",",lst[upp])
        break