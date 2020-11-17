def main():
    option = input("Please Select your option.\n(S) for sign up\n(L) for log in\n")
    valid = False
    while not valid:
        if option.upper() == "L":
            valid = True
            print("Log-in")
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
    valid = False
    cardNum = open("cardNumber.txt", "w")
    while not valid:
        cardNumber = input("Please Enter a card number with 4 unique numbers\n")
        if notSame(cardNumber):
            valid = True
            cardNum.write(cardNumber)
            print("valid")
        else:
            valid = False
            print("Invalid Input, please enter 4 unique numbers")
    cardNum.close()
    



main()
