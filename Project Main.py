import time  # DO NOT REMOVE OR "show()" WILL BREAK


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
    if (number[0] != number[1]) and (number[1] != number[2]) and (number[2] != number[3]) and (
            number[3] != number[0]) and (number[0] != number[2]) and (number[1] != number[3]) and number.isdigit() and (
            len(number) == 4):
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
        email = input("Please enter your email address: \n")
        if email[0:3] == "g20" and email[3:10].isdigit() and email[10:23] == "@kfupm.edu.sa":
            valid = True
            credentials.write("\n" + email)
        else:
            print("Invalid Input, please enter an email with this format:(g20XXXXXXX@kfupm.edu.sa)")
    credentials.write("\n0")
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
    credentials = open("cardNumber.txt", "r")  # *** NOTE: REOPENED THE FILE TO FIX THE RANGE ERROR ***
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
    return cardNum, pinNum  # returns the card number and the PIN number


def show(file):
    credentials = open(file, "r")
    print("\nAccount info:\n")
    print("Card Number: " + credentials.readline())
    print("PIN number: " + credentials.readline())
    print("Email Address: " + credentials.readline())
    print("Current Balance: " + credentials.readline())
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
        if userInput.isdigit():  # Checks if user input is a digit
            valid = True
            if userInput == "1":
                show("cardNumber.txt")
            elif userInput == "2":
                #  cardNum, pinNum = login()  # Gets these two values from the login function. If you look at the two
                # return values, you will hopefully understand
                #  changePINFun(pinNum, cardNum, "cardNumber.txt")
                credentialRead = open("cardNumber.txt", "r")
                cardNumber = credentialRead.readline()
                currentPIN = credentialRead.readline()
                credentialRead.close()
                changePINFun(currentPIN, cardNumber, "cardNumber.txt")

            elif userInput == "3":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "4":
                credentialRead = open("cardNumber.txt", "r")
                cardNumber = credentialRead.readline()
                currentPIN = credentialRead.readline()
                credentialRead.close()
                nMoney = input("Enter amount: ")
                depositFun(nMoney, cardNumber, "cardNumber.txt")

            elif userInput == "5":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "6":
                print("INSERT CODE HERE")  # INSERT CODE HERE!
            elif userInput == "7":
                print("Thank you, come again!")
            else:
                print("Incorrect input! Try again.")
                userInput = input("Enter your feature: ")
        else:
            print("Incorrect input! Try again.")
            userInput = input("Enter your feature: ")


def changePINFun(currentPIN, cardNumber, file):
    valid = False
    while not valid:
        newPIN = input("Enter the new pin:\n")
        if notSame(newPIN):
            credentialRead = open("cardNumber.txt", "r")
            email = ""
            for i in range(3):
                email = credentialRead.readline()
            balance = credentialRead.readline()
            credentialRead.close()
            credentials = open(file, "w")
            credentials.write(cardNumber)
            credentials.write(newPIN + "\n")
            credentials.write(email)
            credentials.write(balance)
            credentials.close()
            valid = True
        else:
            print("Invalid Input, please enter 4 unique numbers")
    time.sleep(2)
    menu()


def depositFun(nMoney, cardNumber, file):
    credentialRead = open("cardNumber.txt", "r")
    pinNum = ""
    for x in range(2):
        pinNum = credentialRead.readline()
    email = credentialRead.readline()
    balance = credentialRead.readline()
    balance.rstrip()
    balance = int(balance)  # Switches from a string to an integer
    balance += int(nMoney)  # Adds the amount to the current balance
    credentialRead.close()
    credentials = open(file, "w")
    credentials.write(cardNumber)
    credentials.write(pinNum)
    credentials.write(email)
    credentials.write(str(balance))  # Switches balance back to a string in order to write it to the file
    credentials.close()
    time.sleep(2)
    menu()


main()
