list=[1,2,3,4,5]
out=[]
for num in list:
    out.append((num))
    out.remove((num))
    print(out)

out=[]
total=sum(list)
for num in list:
    out.append((total-num))
    print(out)


