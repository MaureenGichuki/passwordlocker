from tokenize import Name
from unicodedata import name
from user import User, user
from user import credentials


def create_newuser(username,password):
    new_user=user(username,password)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(name):
    return User.find_user(name)

def display_user():
    return User.user_display()

def create_newcredential(accusername,accname,accpassword):
    new_credential= credential(accusername,accname,accpassword)
    return new_credential