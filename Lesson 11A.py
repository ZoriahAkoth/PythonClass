students = {"P2002": "Jane K", "P2903": "John B"}
admin_no = input("Enter student's admin number : ")
print(students.item())
for key, value in students.item():
    if admin_no == key :
        print("Found")
        break
    else :
        print("Does not exist")
        break

#Another (easier) way 
keys = students.keys()
if admin_no in keys:
    print("Found")
else:
    print("Not found")