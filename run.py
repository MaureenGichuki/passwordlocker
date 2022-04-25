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