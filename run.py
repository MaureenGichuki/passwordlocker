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

def find_user(user):
    return User.find_user(name)

