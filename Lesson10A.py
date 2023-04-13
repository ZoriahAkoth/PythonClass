class Student :
    def register_student_details(self):
        self.name = input("Enter your name : ")
        self.age = input("Enter your age : ")
        self.grade = input("Enter your grade : ")
        self.county = input("Enter your county : ")
        self.gender = input("Enter your gender : ")

    def display_student_details(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.county)
        print(self.gender)

Joe = Student()
Allan = Student()
Mary =Student ()

Joe.register_student_details()
Allan.register_student_details()
Mary.register_student_details()
print("...student information ...")
Joe.display_student_details()
print(".............")
Allan.display_student_details()
print("..........")
Mary.display_student_details()