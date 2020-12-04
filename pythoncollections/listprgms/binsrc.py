lst=[21,20,18,22,7,2,25]
lst.sort()
low=0
upp=len(lst)-1
flg=0
element=int(input("enter the element you want to search"))
while(low<upp):#6
    mid=(low+upp)//2#0+6//2
    #case1
    if(element>lst[mid]):#0<=6
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif element==lst[mid]:
        flg+=1
        break
    if flg==0:
        print("element found")
    else:
        print("element not found")
