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