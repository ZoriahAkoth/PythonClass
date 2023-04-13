#formatting text/string
age = 17
message = "I am {} years old" .format(age)
print(message)
favourite_subject = input("enter favourite subject")
favourite_subject_score = int(input("score for your favourite subject"))
text = "My favourite subject is {}, I scored {} ".format(favourite_subject, favourite_subject_score)
print(text)
#addition
num1 = 20
num2= 30
result =num1 + num2
print(result)

x = 50
y = 40
answer = x - y
print(answer)

z = x * y
print(z)

a = x / y
print(a)

#students Marks
student_name = input("enter your name: ")
Mathematics = float(input("enter your Mathematics score: "))
English = float(input("enter your English score:" ))
Kiswahili = float(input("enter Kiswahili marks: "))
total_marks = Mathematics + English + Kiswahili
Average = total_marks / 3
message = "Hello {} your average score is {}".format(student_name, Average)
print(message)

print("area of rectangle")
length = float(input("enter length "))
width = float(input("enter width "))
area = length * width
print(area)


