#Default constructor

class Student :
    global students_register
    students_register = { }
    def __init__(self, name, age, gender, grade, county, phone):
        #initialize member attributes for this object
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade
        self.county =county
        self.phone = phone
    def register_student(self,name,gender,admin_no):
        students_register [admin_no] = {"name":name,"gender": gender}
        print(students_register)
    def search_student_by_admin_number(self,admin_no):
        for key, value in students_register.items():
            if admin_no == key:
                print("Student record found")
            else:
                print("Student record not found")


Jane = Student("Jane Nduta", 19, "female", "grade 11", "Nairobi", 790484664)
print(Jane.name)
print(Jane.gender)

