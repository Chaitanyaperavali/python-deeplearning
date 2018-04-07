
# System class to handle all operations
# This class is used by all users to perform respective operations
class System(object):

    __staff = []
    __students = []
    __courses = []

    def __init__(self):
        print("Staring System...")

    def perform_operation(self,operation):
        print("performing operation"+operation)

    def get_professor(self,professor_id):
        for s in __class__.__staff:
            if s.__class__.staff_id == professor_id:
                return s

    def get_student(self,student_id):
        for s in __class__.__students:
            if s.__class__.student_id == student_id:
                return s

    def get_course(self,course_id):
        for s in __class__.__courses:
            if s.__class__.course_id == course_id:
                return s

    def add_student(self,student):
        __class__.__students.append(student)

    def add_course(self,course):
        __class__.__courses.append(course)

    def add_staff(self,staff):
        __class__.__staff.append(staff)


# general class staff which is inherited by specific types of staff
class Staff(object):

    staff_id = 0

    def __init__(self,name,department,role):
        self.name = name
        self.department = department
        self.role = role


# Specific staff type inherited from generic staff class
class TeachingStaff(Staff):
    __courses = []

    def __init__(self,name,department,role):
        Staff.__init__(self,name,department,role)
        Staff.staff_id += 1
        #System.add_staff(self)

    def do_research(self):
        print("doing research")

    def teach_course(self,course):
        self.__courses.append(course)
        print("teaching course" + course)

    def assignGrade(self,student,grade,course_id):
        student.getCourse(course_id).grade = grade


# Specific staff type inherited from generic staff class
class NonTeachingStaff(Staff):

    def __init__(self,name,department,role):
        Staff.__init__(self,name,department,role)
        #System.add_staff(self)
        Staff.staff_id += 1

    def do_work(self):
        print("doing work...")


# Cashier is a non-teaching staff
class Cashier(NonTeachingStaff):

    def __init__(self):
        NonTeachingStaff.__init__(department="Financial Services",role="cashier")
        print("Cashier initialized")

    def enroll_student(self,student,course):
        student.courses.append(course)
        course.append(student)


# general class Student which will be inherited by specific types of Student
class Student(object):
    student_id = 1000
    __credits = 0
    __courses = []

    def __init__(self,name,major):
        self.name = name
        self.major = major

    def enroll_course(self,course,credits):
        self.__courses.append(course)
        self.__credits += credits
        print(self.name+" Enrolled in "+course)

    def get_courses_enrolled(self):
        print(self.__courses)

    def get_total_credits(self):
        print(__class__.__credits)


# Full time student inherited from student
class FullTimeStudent(Student):

    def __init__(self,name,major):
        Student.__init__(name,major)
        #System.add_student(self)
        Student.__class__.student_id += 1


# Specific Student- part time type inherited from generic Student class
class PartTimeStudent(Student):

    def __init__(self, name, major):
        Student.__init__(name, major)
        #System.add_student(self)
        Student.__class__.student_id += 1


# student assistant inherited from both student and staff(Multiple Inheritance)
class StudentAssistant(Student,Staff):

    def __init__(self,name,department,role,major):
        Staff.__init__(name,department,role)
        Student.__class__.student_id += 1
        Student.__init__(name,major)
        #System.add_student(self)
        #System.add_staff(self)


class Course(object):
    __course_id = 100

    def __init__(self,name,professor_id):
        self.__course_id += 1
        self.name = name
        System.get_professor(professor_id).teach_course(self)


system = System()
nikhil = TeachingStaff("Nikhil", "CSE", "Assistant Professor")
kk = TeachingStaff("Jone","SCE","Professor")
chaitu = NonTeachingStaff("Chaitanya","IS Labs","Assistant")
course1 = Course("Python/DL",1)
course2 = Course("ASE",1)
course3 = Course("Big data",1)
student1 = Student("Vinod","CS")
student2 = Student("Kalyan","CS")
student1.enroll_course(course1,3)
student1.enroll_course(course2,3)
student1.enroll_course(course3,3)
student2.enroll_course(course2,3)
student1.get_total_credits()
student2.get_total_credits()




