#THE ACTUAL TING
Meeting_ID = int(input("Enter Meeting ID : "))
if Meeting_ID == 123456 :
    Passcode = int(input("Enter meeting passcode : "))
    if Passcode == 2468:
        print(" You have been admitted by the host .")
    else:
        print(" Incorrect Passcode")
else:
    print("Incorrect Meeting ID")
