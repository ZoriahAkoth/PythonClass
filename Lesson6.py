# FOR LOOP
word = "HELLO"
for letter in word:
    print(letter)
for z in range(0, 20):
    print(z)

#repeat password 3 times
for attempt in range(0, 3):
    password = input("Enter password : ")
    if password == "2023":
        print("Login Successful.")
        break
    else:
        print("Incorrect password.Login failed. ")

utensils = ["spoon", "fork", "knife", "plate"]
for item in utensils:
    print(item)