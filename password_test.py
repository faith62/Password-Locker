import unittest # Importing the unittest module
import pyperclip
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

def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Password.password_list = []


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
    '''
    test_save_multiple_password to check if we can save multiple password
    objects to our password_list
    '''
    self.new_password.save_password()
    test_password = Password("user","123456") # new password
    test_password.save_password()
    self.assertEqual(len(Password.password_list),2)  

def test_delete_password(self):
    '''
    test_delete_contact to test if we can remove a contact from our contact list
    ''' 
    self.new_password.save_password()
    test_password = Password("user","123456")#new password
    test_password.save_password()

    self.new_password.delete_password()  #Deleting a contact object
    self.assertEqual(len(Password.password_list),1) 

def text_find_contact_by_number(self):
    '''
    test to check if we can find a password by password and display information
    '''

    self.new_password.save_password()
    test_password = Password("user","345678") #new password
    test_password.save_password()

    found_password = Password.find_by_password("345678")

    self.assertEqual(found_password.user_name,test_password.user_name)

def test_contact_exist(self):
    self.new_password.save_contact()
    test_password = Password("user","345678") #new contact
    test_password.save_password()

    password_exists = Password.password_exist("345678")

    self.assertTrue(password_exists) 

def test_display_all_password(self):
        '''
        method that returns a list of all password saved
        '''

        self.assertEqual(Password.display_password(),Password.password_list)

def test_copy_password(self):
    self.new_password.save_password
    Password.copy_password("123456")

    self.assertEqual(self.new_password.password,pyperclip.paste())



if __name__ == '__main__': #confirming that anything inside the if block should run only if this is the file that is currently being run
    unittest.main() #provides a command line interface that collects all the tests methods and executes them.

