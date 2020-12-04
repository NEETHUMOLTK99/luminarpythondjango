#read csv file
#q1 find yearwise release count


f=open("movies.csv","r")
dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")
    print(data)
    year=data[2]
    break
if year not in dict:
    dict[year]=1
else:
    dict[year]+=1
    print(dict['1992'])
highest=max(dict,key=dict.get)
print(highest,dict[highest])
