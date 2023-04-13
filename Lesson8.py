#Funcions with parameters/ arguments
def addition(num1, num2):
    result = num1 + num2
    print(result)

addition(2,5)
addition(5998,7653)

def greetings(text, surname):
    text_message = text + surname
    print(text_message)

greetings("Hello", "Ahmed")
greetings("Good morning", "Lola")

def validate_password(password):
    special_characters = ["@", "#", "*"]
    if len(password)<6:
        print("Password shouldn't be less than six characters")
    elif not any(char in special_characters for char in password):
        print("Password should contain a special character")
    elif not any(char.isupper() for char in password):
        print("Password should contain a capital letter")
    elif not any(char.isdigit() for char in password):
        print("Password should contain a digit")

validate_password(input("Enter password : "))

name = input ("Enter your name : ")
print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())

fruits = []
for x in range(5):
    fruitname = input("Enter name of the fruit : ").lower()
    fruits.append(fruitname)
print(fruits)
