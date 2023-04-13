#While loop
is_running = False
while is_running:
    print("The game is on")

count = 0
while count < 10:
    print(count)
    count +=1

names = ["John", "Grace", "Ruth", "Josh"]
index_position = 0
length = len(names)
while index_position < length:
    item = names[index_position]
    print(item)
    index_position += 1

#sum of numbers in a list

numbers = [1, 2, 3, 4, 5, 6]
sum = 0
index_position = 0
while index_position < len(numbers):
    sum +=numbers[index_position]
    index_position += 1
print(sum)

attempt = 0
password = "Python23"
while attempt < 3 :
    user_password = input("Enter your password: ")
    if user_password == password:
        print("correct password")
        break
    else :
        print("incorrect password")
    attempt += 1
