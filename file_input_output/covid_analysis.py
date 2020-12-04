f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    print(lines)
    break#1,30/01/20,6:00pm,'kerala',1,0,0,0,1
    words=lines.rstrip("\n").split(",")
    print(words)
    state=words[3]
    cofirmed_cases=words[8]
    if(state not in dict):
        dict[state]=cofirmed_cases
    else:
        dict[state]=cofirmed_cases
for k,v in dict.items():
    print(k,"===>",v)
    high=max(dict,key=dict.get)
print(high,dict[high])