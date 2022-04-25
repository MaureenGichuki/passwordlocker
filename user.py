from collections import UserList


class user:
    """
    This class generates new users
    """

    userlist=[]

    def __init__(self,username,password):

        """
        __init__ method allows the object(self) to be defined

        """
       
        self.username=username
        self.password=password

    def save_user(self):
        """
        the method save_user saves user information into the userlist

        """
        user.userlist.append(self)

    def delete_user(self):
        """
        the method delete_user deletes user from the userlist dict

        """
        user.userlist.remove(self)
    @classmethod
    def user_display(cls):
        """

        the method user_display returns information from the userlist dict

        """
        return cls.userlist
    @classmethod
    def find_user(cls,name):
        """

        the method find_user returns user that matches the name

        """
        for user in cls.userlist:
            if user.username==name:
                return user


class credentials:
    """

    this class instantiates user credentials

    """