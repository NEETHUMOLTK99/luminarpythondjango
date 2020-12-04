employee={"eid":1000,"desig":"developer","exp":1,"company_name":"luminar"}
#print companyname
print(employee["company_name"])
#checking for salary key is there
print("salary" in employee)

#add a new key valuepair salary:30000
employee["salary"]=30000
print(employee)

#Add 5000 more RS to current salary
employee["salary"]+=5000
print(employee)

for emp in employee:
    print(emp)
for k,v in employee.items():
    print(k,",",v)

