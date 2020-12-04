#read data from file named text and display contents here
#to store data
#read r
#write w
#append a

#step-1
#create file reference
#f=open("path","mode of operation")
f=open("text","r")
for lines in f:
    print(lines)

f=open("text","r")
lst=[]
for lines in f:
    lst.append(lines)
    lst.append(lines.rstrip("\n"))
    print(lst)

# f=open("path","mode of operation")
f=open("text","r")
st={}
for lines in f:
    lst.add lines()



