#FUNCTIONS
def addition():
    a = 10
    b = 1
    c = a + b
    print(c)
addition()

def subtraction():
    d = 30
    e = 10
    f = d - e
    print(f)
subtraction()

def send_money():
    balance = 10000
    phone_number = int(input("Enter phone number : "))
    Amount = float(input("Enter Amount : "))
    if Amount < 10 or Amount > 100000:
        print("Cannot send amount.")
    elif Amount > balance:
        print("Cannot send amount.")
    else:
        text_message = "{} has been sent to {}.".format(Amount, phone_number)
        print(text_message)
send_money()