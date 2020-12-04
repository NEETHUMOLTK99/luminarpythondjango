st={}
print(type(st))

st={10,20,30,40,30,20}
print(st)#no duplicates allowed

st={10,20,30,40,40,30}
st1={20,21,22,30}
st.update(st1)
#union set
un=st.union(st1)
print(un)
#intersection
inter=st.intersection(st1)
print(inter)

#difference
diff=st.difference(st1)
print(diff)