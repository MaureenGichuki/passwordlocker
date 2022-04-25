import random
import string

from user import User
from user import Credentials


def create_newuser(username,password):
    new_user= User(username,password)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(namey):
    return User.find_user(namey)

def display_user():
    return User.user_display()

def create_newcredential(accusername,accname,accpassword):
    new_credential= Credentials(accusername,accname,accpassword)
    return new_credential

def save_credential(user):
    user.save_credntial()

def delete_credential(user):
    user.delete_credential()

def find_credential(a_name):
    return Credentials.find_credential(a_name)

def display_user():
    return Credentials.credential_display()

def main():
    while True:
        print("Welcome to your password locker. Key in Sgu -or Lgn for signup or login respectively to continue")
        print("Sgu -or- Lgn")
        option = input()
        if option == "Sgu":
            print("Please enter a Username:")
            username=input()
            print("Please enter desired password:")
            password=input()
            save_user(create_newuser(username,password))
            print("\n")
            print("Hello your password locker has been successfully activated")
            print(f"Username:{username}")
            print(f"Password:{password}")
            print("\n")
            print("You can now use you details to login")     
        elif option == "Lgn":
            print("\n")
            print("Enter username")
            username=input()
            print("Enter password")
            password=input()
            if find_user(username):
                print("\n")
                print("Create new account or View existing accounts key in add exist for adding accounts or viewing existing accounts respectively")
                print("\n")
                print(" add -or- exist")
                selection =input()
                if selection == "add":
                    print("\n")
                    print("Add an account")
                    print("Enter account name")
                    accname=input()
                    accusername=username
                    print("Create password or Get an automatic password. Enter Cp or Gp for both options respectively")
                    print("Cp -or- Gp")
                    choice = input()
                    if choice == "Cp":
                        print("Enter password")
                        accpassword=input()
                        print("\n")
                    elif choice == "Gp":
                        letters = string.ascii_lowercase
                        accpassword="".join(random.choice(letters) for i in range(7))
                        print(f"Password:{accpassword}")
                        print("\n")
                    print(f"Username:{accusername}")
                    print(f"Account name:{accname}")
                    print(f"Account password:{accpassword}")
                    print("\n")
                elif selection == "exist":
                    if find_credential(accname):
                        print("Here are your accounts:")
                        for user in display_user():
                            print(f"Account:{user.accname}")
                            print("\n")
                            print(f"Username:{user.accusername}")
                            print("\n")
                            print(f"Password:{user.accpassword}")
                            
            else:  print("Would you like to sign out")
            print("Would you like to sign out yes")
            decision=input()
            if decision =="yes":
                print("Thanks for choosing passwordlocker!")

if __name__ == "__main__":
    main()
