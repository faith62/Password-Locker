import pyperclip
from keyring import delete_password


class User:
    """
    Class that generates new instances of password
    """
    user_list = [] #used to store our created user objects 

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves password objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns password list
        '''
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)

        
class Password:
    """
    Class that generates new instances of password
    """
    password_list =  [] #used to store our created password objects 

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)
        

    def delete_password(self):
        '''
        delete_password method deletes a saved contact from the password_list
        '''

        Password.password_list.remove(self)

    @classmethod
    def find_by_password(cls,number):
        for password in cls.password_list:
            if password.password == password:
                return password

    @classmethod
    def password_exist(cls,password):
        for password in cls.password_list:
            return True

        return False

    @classmethod
    def display_password(cls):
        '''
        method that returns password list
        '''
        return cls.contact_list

    @classmethod
    def copy_password(cls,password):
        password_found = Password.find_by_password(password)
        pyperclip.copy(password_found.password) #copy passed in items to the machines clipboard
