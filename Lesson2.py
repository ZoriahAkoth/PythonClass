# joining strings
first_name = input("enter first name: ")
second_name = input("enter second name: ")
fullname = first_name + " " + second_name
print(fullname)
# surname, greeting, message
surname = input("enter parent's surname: ")
salutation = input("Mr/Mrs/Miss/Sir/Madam ")
greeting = input("Good morning / Good evening / Good afternoon ")
text_message = greeting + " " + salutation + " " + surname + " " + "you are invited to our PTA metting on Saturday at 10am "
print(text_message)
# recipient name, amount, new balance, time
# xx amount has
send_amount = input("enter amount to send ")
recipient_number = input("enter phone number")
mpesa_message = "Ksh. " + send_amount + " has been sent to " + recipient_number
print(mpesa_message)
