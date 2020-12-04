#print student names

students=[

    [100,"arun","bca",145],
    [101,"arjun","bca",125],
    [102,"varun","mca",150],
    [103,"tinu","mca",140],
    [104,"jeena","bcom",120],]
for student in students:
    print(student[1])
#print student names
for student in students:
#[100,"arun","bca",145]
    print(student[1])
#print total of all students
student=[]
total=0
for student in students:
    total=total+student[3]
    print(total)

#list the details of student whose course mca
for student in students:
    if student[2]=='mca':
        print(student)
#mca?bca?bcom?
mtotal=btotal=ctotal=0
for student in students:
    if student[2]=='mca':
        mtotal+=1
    elif student[2]=='bcom':
        btotal=+1
    elif student[2]=='bca':
        ctotal+=1
        print("number of students in mca",mtotal)
        print("number of students in bcom",btotal)
        print("number of students in bca",ctotal )
#print highest total




