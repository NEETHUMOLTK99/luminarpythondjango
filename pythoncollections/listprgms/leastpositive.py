
lst=[-2,-1,0,1,2,3,4]
cnt=1
for i in range(0,len(lst)):
    if cnt in lst:
        if(cnt>1):
            cnt+=1
    else:
        print(cnt, "is missing least positive integer")
        break
#or

lst=[-2,-1,0,1,2,3,4]
cnt=1
for i in range(0,len(lst)):
    if cnt in lst:
            cnt+=1
    else:
        print(cnt, "is missing least positive integer")
        break

print(1 in lst)#check for 1 in list or not



    if cnt in lst:
        if(cnt>1):
            cnt+=1
    else:
        print(cnt, "is missing least positive integer")
        break













