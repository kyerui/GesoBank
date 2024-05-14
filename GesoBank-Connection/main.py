from Services import Account, User, Card, Transference, Loan
from Miscellaneous import ascii_logo

def nav_logged():
    while True:
        match int(input("\n### YOUR ACCOUNT ###\n1: Balance\n2: User Data\n3: Register Card\n4: Get Card\n5: Delete Card\n6: Loan\n7: Transference\n8: Loggof\n\nSelect one of the options above: ")):
            case 1:
                print("\nMY BALANCE")
                User.get_user_balance()
            case 2:
                print("\nUSER INFO")
                User.get_user_data()
            case 3:
                print("\nREGISTER CARD")
                Card.register_card()
            case 4:
                print("\nCARD INFO")
                Card.get_card()
            case 5:
                print("\nDELETE CARD")
                Card.delete_card()
            case 6:
                print("\nLOAN")
                Loan.loan()
            case 7:
                print("\nTRANSFERENCE")
                Transference.transference()
            case 8:
                break

def nav_starts():
     while True:
        ascii_logo.print_logo()
        match int(input("\n1: Login\n2: Register\n3: Exit\n\nSelect one of the options above: ")):
            case 1:
                print("\nLOGIN")
                if Account.login(): nav_logged()
            case 2:
                print("\nREGISTER")
                Account.register_user()
            case 3:
                print("Exiting...")
                break

if __name__ == "__main__":
    nav_starts()
