#find second largest from list
lst=[1,2,3,4,5,6]
num=5
length=len(lst)
for i in range(0,num):
    if(i>num):
        num=+1
print(lst[num])
print(num,"second largest number is")

#or
#sort this array
lst=[12,50,35,45,20]
lst.sort(reverse=True)#method
print(lst[1])


sorted(lst)#function


