from user import user
from user import credentials


def create_newuser(username,password):
    new_user=user(username,password)
    return new_user