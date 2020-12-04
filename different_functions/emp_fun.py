#create a function print_employee_data()
#step1 process the file and store it into dictionary
employee={}
f=open("employee","r")
for lines in f:

    employee_data=lines.rstrip("\n").split(",")
    print(employee_data)

#if we pass id    as argument that function will print employee name

    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    employee[id]={"id":id,"name":name,"exp":exp,"salary":salary}
for k,v in employee.items():
    print(k,v)

def print_employee_data(**kwargs):
    print(kwargs)
    if"id" in kwargs:

