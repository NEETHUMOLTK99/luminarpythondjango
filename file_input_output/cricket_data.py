f=open("data","r")
lst=[]
for lines in f:
    words=lines.split(" ")
    for word in words:
        lst.append(word.rstrip(".\n"))
print(lst)



#wordcount
f=open("data","r")
dict={}
for lines in f:
    words=lines.rstrip(".\n").split(" ")#Zampa comes back on.\n
    print(words)
    #['zampa', 'comes ','back ','on'
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)

#find highest frequency word
#method1
lst=[]
for(k,v) in dict.items():
    lst.append(v)
high=max(lst)

for k,v in dict.items():
    if(v==high):
        print(k,v)
#method 2
high=max(dict,key=dict.get)
print(high)
