#if and else
age = int(input("Enter you age: "))
if age > 17:
    print("an adult")
else:
    print("a child")

x = int(input("enter x : "))
y = int(input ("enter y : "))
if x > y:
    print("{} is greater than {}".format(x,y))
else:
    print("{} is not greater than {}".format(x, y))

user_password = input("enter your password: ")
if user_password == "python22":
    print("Access granted.")
else:
    print("Wrong password. Access denied.")

#school grading sys
# 80 - 100 A, 60 - 79 B, 40 - 59 C
Mathematics = float(input("Enter your Mathematics score : "))
if Mathematics < 0 or Mathematics > 100 :
    print("Invalid entry! Try again")
elif Mathematics >= 80 and Mathematics <= 100 :
    print("A")
elif Mathematics >= 60 and Mathematics <= 80 :
    print("B")
elif Mathematics >= 40 and Mathematics <= 60 :
    print("C")
else:
    print("D")

#searching for items in a list
fruits = ["mango", "apple", "pawpaw", "pineapple"]
fruit_name = input("enter fruit : ")
if fruit_name in fruits:
    print("{} is available".format(fruit_name))
else:
    print("{} is not available".format(fruit_name))
    add_fruit = input("Do you want to add {} to you fruits list? (yes/no)".format(fruit_name))
    if add_fruit == "yes":
        fruits.append(fruit_name)
        print("Fruit added successfully")
    else:
        print("Okay.")




