import unittest # Importing the unittest module
import pyperclip
from password import User
from password import Credentials # Importing the credentials class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self): #allows us to define instructions that will be executed before each test method.
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Faith", "123456") # create new instance of user class, store in an instance variable in test class self.new_user

def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.user_name,"Faith")
    self.assertEqual(self.new_user.password,"123456")

def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self): #allows us to define instructions that will be executed before each test method.
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Faith", "123456") # create new instance of credentials class, store in an instance variable in test class self.new_credentials

def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_credentials.account,"Instagram")
    self.assertEqual(self.new_credentials.user_name,"Faith")
    self.assertEqual(self.new_credentials.password,"cfi12")

def test_save_credentials(self):
    '''
    test_save_credentials test case to test if the credentials object is saved into
        the credentials list
    '''
    self.new_credentials.save_credentials() # saving the new credentials
    self.assertEqual(len(Credentials.credentials_list),1)

def test_save_multiple_credentials(self):
    '''
    test_save_multiple_credentials to check if we can save multiple credentials
    objects to our credentials_list
    '''
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Facebook","Fchem","fchem1") # new credentials
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)  

def test_delete_credentials(self):
    '''
    test_delete_contact to test if we can remove a contact from our contact list
    ''' 
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Facebook","Fchem","fchem1")#new credentials
    test_credentials.save_credentials()

    self.new_credentials.delete_credentials()  #Deleting a contact object
    self.assertEqual(len(Credentials.credentials_list),1) 

def text_find_credential_by_account(self):
    '''
    test to check if we can find a credentials by credentials and display information
    '''

    self.new_credentials.save_credentials()
    test_credentials = Credentials("Facebook","Fchem","fchem1") #new credentials
    test_credentials.save_credentials()

    found_credentials = Credentials.find_by_credentials("Facebook")

    self.assertEqual(found_credentials.account,test_credentials.account)

def test_credential_exist(self):
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Facebook","Fchem","fchem1") #new contact
    test_credentials.save_credentials()

    credentials_exists = Credentials.credentials_exist("Facebook")

    self.assertTrue(credentials_exists) 

def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

def test_copy_credentials(self):
    self.new_credentials.save_credentials
    Credentials.copy_credentials("Instagram")

    self.assertEqual(self.new_credentials.credentials,pyperclip.paste()) # returns whatever is copied on the machine's clipboard at that time.



if __name__ == '__main__': #confirming that anything inside the if block should run only if this is the file that is currently being run
    unittest.main() #provides a command line interface that collects all the tests methods and executes them.

