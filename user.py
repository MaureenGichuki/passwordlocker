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