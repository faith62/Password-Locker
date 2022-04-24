import unittest # Importing the unittest module
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self): #allows us to define instructions that will be executed before each test method.
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("Faith", "123456") # create new instance of password class, store in an instance variable in test class self.new_password


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_password.user_name,"Faith")
    self.assertEqual(self.new_password.password,"123456")

def test_save_password(self):
    '''
    test_save_password test case to test if the password object is saved into
        the password list
    '''
    self.new_password.save_password() # saving the new password
    self.assertEqual(len(Password.password_list),1)

def test_save_multiple_password(self):
    self.new_password.save_password()
    test_password = Password("user","123456") #new password
    test_password.save_password()
    self.assertEqual(len(Password.password_list),2)


    

if __name__ == '__main__': #confirming that anything inside the if block should run only if this is the file that is currently being run
    unittest.main() #provides a command line interface that collects all the tests methods and executes them.

