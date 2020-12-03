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
    if len(number) == 4:
        valid = False
        if (number[0] != number[1]) and (number[1] != number[2]) and (number[2] != number[3]) and (number[3] != number[0]) and (number[0] != number[2]) and (number[1] != number[3]) and number.isdigit() and (len(number) == 4):
            valid = True
    else:
        valid = False
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


def menu():  # NOT DONE YET
    valid = False
    while not valid:
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
        credentialRead = open("cardNumber.txt", "r")
        cardNumber = credentialRead.readline()
        currentPIN = credentialRead.readline()
        email = credentialRead.readline()
        balance = credentialRead.readline()
        credentialRead.close()
        userInput = input("Enter your feature: ")
        if userInput == "1":
            show("cardNumber.txt")  # 1. Show account information
            time.sleep(2)  # Waits 2 seconds

        elif userInput == "2":  # 2. Change PIN number
            changePINFun(currentPIN, cardNumber, "cardNumber.txt")
            time.sleep(2)  # Waits 2 seconds

        elif userInput == "3":  # 3. Withdraw amount of money
            flag = False
            while not flag:
                money = input("Enter amount: ")
                if money.isalpha() or float(money) < 0:
                    print("Invalid input")
                else:
                    flag = True
                    withdrawFun(money, cardNumber, "cardNumber.txt")
            time.sleep(2)  # Waits 2 seconds

        elif userInput == "4":  # 4. Deposit amount of money
            flag = False
            while not flag:
                nMoney = input("Enter amount: ")
                if nMoney.isalpha() or float(nMoney) < 0:
                    print("Invalid input")
                else:
                    flag = True
                    depositFun(nMoney, cardNumber, "cardNumber.txt")
            time.sleep(2)  # Waits 2 seconds

        elif userInput == "5":  # 5. Pay bills
            nMoney = 0
            payBillFun("cardNumber.txt", nMoney, cardNumber)
            time.sleep(2)  # Waits 2 seconds

        elif userInput == "6":  # 6. View the last transactions
            viewTransactionsFun(0)
            time.sleep(2)  # Waits 2 seconds

        elif userInput == "7":  # 7. Terminate a program
            terminateFun("transactions.txt", balance, cardNumber)
            break  # Exits from the loop

        else:  # invalid input
            print("Incorrect input! Try again.")


def changePINFun(currentPIN, cardNumber, file):
    valid = False
    while not valid:
        newPIN = input("Enter the new pin:\n")
        if notSame(newPIN):
            credentialRead = open("cardNumber.txt", "r")
            email = ""
            for i in range(3):
                email = credentialRead.readline()  # Reads line number 3
            balance = credentialRead.readline()  # Reads line number 4
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


def depositFun(nMoney, cardNumber, file):
    credentialRead = open(file, "r")
    pinNum = ""
    for x in range(2):
        pinNum = credentialRead.readline()
    email = credentialRead.readline()
    balance = credentialRead.readline()
    balance.rstrip()
    balance = float(balance)  # Switches from a string to a float
    balance += float(nMoney)  # Adds the amount to the current balance
    credentialRead.close()
    credentials = open(file, "w")
    credentials.write(cardNumber)
    credentials.write(pinNum)
    credentials.write(email)
    credentials.write("%.2f" % balance)  # Switches balance back to a string and formats it to 2 decimals
    credentials.close()
    #  add transaction to log
    localtime = time.localtime()
    timeNow = time.strftime("%I:%M:%S %p", localtime)
    lastTransactionWrite = open("lastTransaction.txt", "w")  # Opens the last transaction file as an empty file
    lastTransactionWrite.write(("[" + timeNow + "] +" + nMoney + "\n"))  # formats the line, like adding time and such
    lastTransactionWrite.close()
    lastTransactionRead = open("lastTransaction.txt", "r")  # Opens the file again but in read mode to get the line
    line = lastTransactionRead.readline()
    lastTransactionRead.close()
    transactionsFile = open("transactions.txt", "a")  # Opens in append mode to add the last transaction into
    # the transaction file
    transactionsFile.write(line)
    transactionsFile.close()


def withdrawFun(money, cardNumber, file):
    credentialRead = open(file, "r")
    pinNum = ""
    for x in range(2):
        pinNum = credentialRead.readline()
    email = credentialRead.readline()
    balance = credentialRead.readline()
    balance.rstrip()
    balance = float(balance)  # Switches from a string to a float
    valid = False
    while not valid:
        if float(money) > balance:  # Checks if the withdraw amount is higher than the current balance
            print("Your balance is too low to withdraw that amount\n")
            money = input("Enter amount: ")
        else:
            balance -= float(money)  # Withdraws from the current balance
            valid = True
    credentialRead.close()
    credentials = open(file, "w")
    credentials.write(cardNumber)
    credentials.write(pinNum)
    credentials.write(email)
    credentials.write("%.2f" % balance)  # Switches balance back to a string and formats it to 2 decimals
    credentials.close()
    #  add transaction to log
    localtime = time.localtime()
    timeNow = time.strftime("%I:%M:%S %p", localtime)
    lastTransactionWrite = open("lastTransaction.txt", "w")  # Opens the last transaction file as an empty file
    lastTransactionWrite.write(("[" + timeNow + "] -" + money + "\n"))  # formats the line, like adding time and such
    lastTransactionWrite.close()
    lastTransactionRead = open("lastTransaction.txt", "r")  # Opens the file again but in read mode to get the line
    line = lastTransactionRead.readline()
    lastTransactionRead.close()
    transactionsFile = open("transactions.txt", "a")  # Opens in append mode to add the last transaction into
    # the transaction file
    transactionsFile.write(line)
    transactionsFile.close()



def viewTransactionsFun(cardNumber):
    transactionRead = open("transactions.txt", "r")
    transactions = transactionRead.readlines()
    for i in range(len(transactions)):
        print(transactions[i])


def payBillFun(file, nMoney, cardNumber):
    billName = input("Enter the bill name:\n")
    #  validates bill Number
    billNumber = input("Enter the bill account number:\n")
    while not notSame(billNumber):
        if not notSame(billNumber):
            print("Invalid Input, please enter 4 unique numbers")
        billNumber = input("Enter the bill account number:\n")

    valid = False
    while not valid:
        nMoney = input("Enter the amount of money in the bill:\n")
        if nMoney.isalpha() or float(nMoney) < 0:
            print("Invalid input")
        else:
            credentialRead = open(file, "r")
            pinNum = ""
            for x in range(2):
                pinNum = credentialRead.readline()
            email = credentialRead.readline()
            balance = credentialRead.readline()
            balance.rstrip()
            balance = float(balance)  # Switches from a string to a float
            valid = False
            while not valid:
                if float(nMoney) > balance:  # Checks if the withdraw amount is higher than the current balance
                    print("Your balance is too low to withdraw that amount\n")
                    nMoney = input("Enter the amount of money in the bill:\n")
                else:
                    balance -= float(nMoney)  # Withdraws from the current balance
                    valid = True
            credentialRead.close()
            credentials = open(file, "w")
            credentials.write(cardNumber)
            credentials.write(pinNum)
            credentials.write(email)
            credentials.write("%.2f" % balance)  # Switches balance back to a string and formats it to 2 decimals
            credentials.close()
            #  add transaction to log
            localtime = time.localtime()
            timeNow = time.strftime("%I:%M:%S %p", localtime)
            lastTransactionWrite = open("lastTransaction.txt", "w")
            lastTransactionWrite.write(
                ("[" + timeNow + "] -" + nMoney + " to " + billName + " with bill number: " + billNumber + "\n"))
            lastTransactionWrite.close()
            lastTransactionRead = open("lastTransaction.txt", "r")
            line = lastTransactionRead.readline()
            lastTransactionRead.close()
            transactionsFile = open("transactions.txt", "a")  # Opens in append mode to add the last transaction into
            # the transaction file
            transactionsFile.write(line)
            transactionsFile.close()
            valid = True




def terminateFun(file, nMoney, cardNumber):
    lastTransaction = open("lastTransaction.txt", "r")
    line = lastTransaction.readline()
    if line == "":
        print("No transactions were made during this session.")
    else:
        print("This is you last Transaction:\n\n" + line)
    print("Thank you, come again!")


lastTransaction = open("lastTransaction.txt", "w")
lastTransaction.write("")
lastTransaction.close()
main()
