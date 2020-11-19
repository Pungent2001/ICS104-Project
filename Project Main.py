def main():
    option = input("Please Select your option.\n(S) for sign up\n(L) for log in\n")
    valid = False
    while not valid:
        if option.upper() == "L":
            valid = True
            print("Log-in")
            login()
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
            valid = False
            print("Invalid Input, please enter 4 unique numbers")
    # Function to enter pin to card
    valid = False
    while not valid:
        pinNumber = input("Please Enter a pin number with 4 unique numbers\n")
        if notSame(pinNumber):
            valid = True
            credentials.write("\n" + pinNumber)
        else:
            valid = False
            print("Invalid Input, please enter 4 unique numbers")
    # Function to take email
    valid = False
    while not valid:
        email = input("Please enter your email address: ")
        if email[0:3] == "g20" and email[3:10].isdigit() and email[10:23] == "@kfupm.edu.sa":
            valid = True
            credentials.write("\n" + email)
        else:
            print(email[0:3])
            print(email[3:10])
            print(email[10:23])
            valid = False
            print("Invalid Input, please enter an email with this format:(g20XXXXXXX@kfupm.edu.sa)")
    print("Account successfully created!\n")


def login():
    # Uses user input to log-in
    credentials = open("cardNumber.txt", "r")
    cardNumberLogIn = input("Please enter your card number: \n")
    valid = False
    while not valid:
        if (credentials.readline(1)) == cardNumberLogIn:
            valid = True
            print("valid")
        else:
            print("invalid")
            print(credentials.readline(1))
            cardNumberLogIn = input("Please enter your card number: \n")
    print("abc")


main()
