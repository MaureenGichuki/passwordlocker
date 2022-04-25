from collections import UserList


class User:
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
        User.userlist.append(self)

    def delete_user(self):
        """
        the method delete_user deletes user from the userlist dict

        """
        User.userlist.remove(self)

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
    credentiallist=[]
    def __init__(self,accusername,accname,accpassword):
            """

            the method defines properties of the account

            """
            self.accusername=accusername
            self.accname=accname
            self.accpassword=accpassword

    def save_credential(self):
        """
        the method save_credential saves credential information into the credentiallist dict

        """
        credentials.credentiallist.append(self)
    
    def delete_credential(self):
        """
        the method delete_credential deletes account information from the credentiallist dict

        """
        credentials.credentiallist.remove(self)

    @classmethod
    def credential_display(cls):
        """

        the method credential_display returns information from the userlist dict

        """
        return cls.credentiallist

    @classmethod
    def find_credential(cls,a_name):
        """

        the method find_credential returns an account that matches the name

        """
        for credential in cls.credentiallist:
            if credential.accname==a_name:
                return credential