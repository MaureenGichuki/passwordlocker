import unittest
from user import User

class Usertest(unittest.TestCase):

    """
    this class test each case from the user class

    """
def setUp(self):

    """

    the method setUp runs before each case in the user class

    """
    self.newuser= User("maureen123","hey123")

def inittest(self):

    """
    test to confirm if the object user has been initialized correctly

    """
    self.assertEqual(self.newuser.username,"maureen123")

    self.assertEqual(self.newuser.password,"hey123")