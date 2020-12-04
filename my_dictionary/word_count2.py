dict={}
pattern="ABABAC"
for word in pattern:
    if (word not in dict):
        dict[word]=1


    else:
        if(word in dict):
            dict[word]=+1
print(dict)



#first recursive charachter
dict={}
for char in pattern:
    if char not in dict:
        dict[char]=1
    else:
        print("recursive charachter is",char)
        break
