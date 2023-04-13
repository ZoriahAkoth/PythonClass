class Employee:
    def __init__(self, name,  gender, experience, role, salary):
        self.name = name
        self.gender = gender
        self.experience = experience
        self.salary = salary
        self.role = role

    def check_profile (self):
        print("Employee profile")
    def calculate_salary(self):
        print("Salary calculator function")

class Manager(Employee):
    def fire (self):
        print("Manager can fire")
    def hire(self):
        print("Manager can hire")

manager = Manager("Kendi Kira", "Female", 5 ,"Manager", 100000)
manager.check_profile()
manager.calculate_salary()
employee = Employee("Joe", "Male", 8, "staff", 120000)

class Company:
    def __init__(self, name, address, telephone, total_employees, manager):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.total_employees = total_employees
        self.manager = manager
    def services(self):
        x = ["fixed data", "voice", "web_hosting"]
        print(x)
    def community_works(self):
        print("Community empowermebt programs")
    def increase_employee_count(self, new_count):
        self.total_employees += new_count
    def decrease_employee_count(self, deducted_count):
        self.total_employees -= deducted_count

class CompanyBranch(Company):
    def selling_phones(self):
        print("This branch sells phones")
    def customer_care_shop(self):
        print("Customer care is available at the branch")

branch = CompanyBranch( )

