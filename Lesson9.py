#Classes
class Person :
    name = "Lola Chad"
    age = 17
    nationality = "Ethiopian"
    phone = "0715248633"

    def speaks():
        print("A person speaks")
    def befriend():
        friend_name = input("Enter your new friend : ")
        print("The person is now a friend to {}".format(friend_name))
    def has_job():
        print("A person works at a job")

print(Person.name)
print(Person.nationality)
Person.gender = "Female"
print(Person.gender)
Person.name = "Brandon"
Person.gender = "Male"
Person.age = 21
print(Person.name)
print(Person.age)
print(Person.gender)

Person.speaks()
Person.befriend()
Person.has_job()

class BankAccount:
    account_name = "Jane Njuguna"
    account_number = 12345678
    global balance
    balance = 1239000
    dateopened = "12/12/2023"
    branch = "Karen"

    def check_balance ():
        print(balance)
    def deposit():
        amount = float(input("Enter amount you wish to deposit : "))
        print(amount)

BankAccount.check_balance()
BankAccount.deposit()

class student:
    Name = "Joy Wambui"
    Age = 16
    Gender = "Female"
    School = "The Kenya High School"
    Class = "Form 4 East"

    def check_grade ():
        grade = input("Enter student's final grade:")
        print(grade)
student.check_grade()
print(student.Name)