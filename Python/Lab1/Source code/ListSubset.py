def studentsCommonInBothCourses(listPython,listWebApp):
    commonStudents = []
    uCommonStudents = []

    students = []

    # iterate over Python list and add students to new list
    for student in listPython:
        if(student in listWebApp):
            commonStudents.append(student)
        else:
            uCommonStudents.append(student)

    #Append all student types into student
    students.append(commonStudents)
    students.append(uCommonStudents)

    return students

studentlist = studentsCommonInBothCourses(["jane","ash","valli","nishi","kishi"],["ash","valli","nishi"])

# print students
print("Common students: ")
for x in studentlist[0]:
    print(x)
print("\nNot Common students: ")
for x in studentlist[1]:
    print(x)