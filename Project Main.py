import time # DO NOT REMOVE OR "show()" WILL BREAK

def main():
    option = input("Please Select your option.\n(S) for sign up\n(L) for log in\n")
    valid = False
    while not valid:
        if option.upper() == "L":
            valid = True
            login()
            menu()
            # Log-in Function
        elif option.upper() == "S":
            valid = True
            create()
            # Sign-up Function
        else:
            valid = False
            print("Invalid Option, please enter either S or L\n" + "#" * 43)
            option = input("(S) for sign up\n(L) for log in\n")
            # Repeat loop if the input is invalid


def notSame(number):
    # Function to verify all 4 numbers entered by user are unique
    valid = False
    if (number[0] != number[1]) and (number[1] != number[2]) and (number[2] != number[3]) and (number[3] != number[0]) and (number[0] != number[2]) and (number[1] != number[3]) and number.isdigit() and (len(number) == 4):
        valid = True
    return valid


def create():
    # Function to make the user sign-up
    # Function to enter card number
    valid = False
    credentials = open("cardNumber.txt", "w")
    while not valid:
        cardNumber = input("Please Enter a card number with 4 unique numbers\n")
        if notSame(cardNumber):
            valid = True
            credentials.write(cardNumber)
            print("valid")
        else:
            print("Invalid Input, please enter 4 unique numbers")
    # Function to enter pin to card
    valid = False
    while not valid:
        pinNumber = input("Please Enter a pin number with 4 unique numbers\n")
        if notSame(pinNumber):
            valid = True
            credentials.write("\n" + pinNumber)
        else:
            print("Invalid Input, please enter 4 unique numbers")
    # Function to take email
    valid = False
    while not valid:
        email = input("Please enter your email address: ")
        if email[0:3] == "g20" and email[3:10].isdigit() and email[10:23] == "@kfupm.edu.sa":
            valid = True
            credentials.write("\n" + email)
        else:
            print("Invalid Input, please enter an email with this format:(g20XXXXXXX@kfupm.edu.sa)")
    print("Account successfully created!\n")
    credentials.close()
    menu()


def login():
    # validates user card to log in
    credentials = open("cardNumber.txt", "r")
    valid = False
    cardNum = credentials.readlines()[0]
    while not valid:
        cardNumberLogIn = input("Please enter your card number: \n")
        if cardNum == str(cardNumberLogIn + "\n"):
            valid = True
        else:
            print("Incorrect Credentials, please try again")
    credentials.close()
    # validates user pin to log in
    credentials = open("cardNumber.txt", "r") # *** NOTE: REOPENED THE FILE TO FIX THE RANGE ERROR ***
    print("Correct Card number")
    valid = False
    pinNum = credentials.readlines()[1]
    while not valid:
        pinNumberLogIn = input("Please enter your PIN number: \n")
        if pinNum == str(pinNumberLogIn + "\n"):
            valid = True
        else:
            print("Incorrect Credentials, please try again")
    print("Correct PIN")
    return (cardNum, pinNum) # returns the card number and the PIN number


def show(file):
    credentials = open(file, "r")
    print("\nAccount info:\n")
    lineNum = 1 # This is a line counter
    for line in credentials:
        line.rstrip()
        if lineNum == 1: # If line number equals 1
            print("Card number:", line)
        elif lineNum == 2: # If line number equals 2
            print("PIN number:", line)
        else: # line 3 is the last line so there's no need to put an "elif"
            print("Email:", line)
        lineNum += 1
    credentials.close()
    time.sleep(2)  # Waits 2 seconds
    menu()


def menu():  # NOT DONE YET
    print("\nBank Account Program")
    print("=================================")
    print("1. Show account information")
    print("2. Change PIN number")
    print("3. Withdraw amount of money")
    print("4. Deposit amount of money")
    print("5. Pay bills")
    print("6. View the last transactions")
    print("7. Terminate a program")
    print("=================================")

    userInput = input("Enter your feature: ")
    valid = False
    while not valid:
        if userInput.isdigit(): # Checks if user input is a digit
            valid = True
            if userInput == "1":
                show("cardNumber.txt")

            elif userInput == "2":
                cardNum, pinNum = login() # Gets these two values from the login function. If you look at the two return values, you will hopefully understand
                changePINFun(pinNum, cardNum, "cardNumber.txt")

            elif userInput == "3":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "4":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "5":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "6":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "7":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            else:
                print("Incorrect input! Try again.")
                userInput = input("Enter your feature: ")
        else:
            print("Incorrect input! Try again.")
            userInput = input("Enter your feature: ")


def changePINFun(currentPIN, cardNumber, file):
    credentials = open(file, "r")
    valid = False
    while not valid:
        newPin = input("Please enter your new PIN number with 4 unique numbers (Press enter to cancel): ")
        if newPin == "": # If the user pressed enter then it will redirect them back to the menu after 2 seconds
            valid = True
            time.sleep(2) # Waits 2 seconds
            menu()
        elif notSame(newPin): # validates the new PIN
            valid = True
            print("SUCCESS!")
            overwriteLine = ""
            for line in credentials:
                overwriteLine += line
            overwriteLine = overwriteLine.replace(currentPIN, newPin + "\n")
            credentials.close()
            credentials = open(file, "w")
            credentials.write(overwriteLine)
            # Insert a code that replaces the old PIN with the new PIN here
        else:
            print("Invalid Input, please enter 4 unique numbers")


main()
