text='hai how are you hai how are you'
text.split(" ")
dict={}
words='hai how are you hai how are you'
for word in words:
    if (word not in dict):#if hai is not in dict
        dict[word]=1
    else:
        if (word in dict):

            dict[word]=+1

print(dict)
