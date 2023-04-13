class Employee:
    def __init__(self, name, gender , role):
        self.name = name
        self.gender = gender
        self.role = role
    def show_profile(self):
        print(f"name: {self.name} \n gender : {self.gender} \n role : {self.role}")

class SwareDeveloper(Employee):
    def __init__(self, name, gender, role, prog_lang, github_username):
        super().__init__(name,gender,role)
        self.prog_lang = prog_lang
        self.github_username = github_username
    def show_github_details(self):
        print(f"github_username :{self.github_username}")


worker = Employee(" Hassan Juma", "Male", "Marketing Manger")
swaredev = SwareDeveloper("Jane Yuma", "Female", "Software Developer", "Python" , "JYuma")

worker.show_profile()
swaredev.show_github_details()