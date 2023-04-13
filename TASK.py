class Employee:
    def __init__(self, first_name, last_name, gender, staff_ID, role):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.staff_ID = staff_ID
        self.role = role
        self.leave_days_taken = 0
        self.leave_days_pending = 0
        self.years_of_experience = 0

    def calculate_leave_days(self):
        print(f"Leave days taken : {self.leave_days_taken}")
        print(f"Leave days pending : {self.leave_days_pending}")

    def calculate_bonus (self, salary, years_of_experience):
        if self.years_of_experience > 5:
            bonus = 0.6 * salary
        elif self.years_of_experience > 3:
            bonus = 0.45 * salary
        elif self.years_of_experience > 2:
            bonus = 0.3 * salary
        else:
            bonus = 0.25 * salary
        return bonus

worker = Employee("Matthew", "Struat","Male"," P0054","Accountant")
worker.leave_days_taken = 5
worker.leave_days_pending = 25
worker.years_of_experience = 4
worker.calculate_leave_days()
bonus = worker.calculate_bonus(50000, worker.years_of_experience )
print(f"Total salary : {bonus}")

