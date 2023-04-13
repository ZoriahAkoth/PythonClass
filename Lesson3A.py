send_amount = float(input("enter amount to send"))
mobile_number = input(" enter mobile phone number ")
balance = 1000.00
balance -= send_amount
mpesa_message = "You have sent {} to {} new balance is {} ".format(send_amount, mobile_number, balance)
print(mpesa_message)

house_allowance = float(input("enter house allowance "))
commuter_allowance = float(input("enter commuter allowance "))
car_allowance = float(input("enter car allowance "))
basic_salary = float(input("enter basic salary "))
gross_salary = house_allowance + car_allowance + commuter_allowance + basic_salary
tax = 0.3 * gross_salary
print(tax)



