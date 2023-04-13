first_name = input("enter first name ")
surname = input("enter surname ")
employee_name = first_name + " " + surname
salary = float(input("enter salary "))
tax = salary * 0.2
text_message = "Dear {}, your due tax amount is {} ".format(employee_name, tax)
print(text_message)