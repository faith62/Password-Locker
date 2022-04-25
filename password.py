import pyperclip
# from keyring import delete_credentials


class User:
    """
    Class that generates new instances of user
    """
    user_list = [] #used to store our created user objects 

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns user list
        '''
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)

        
class Credentials:
    """
    Class that generates new instances of password
    """
    credentials_list =  [] #used to store our created credentials objects 

    def __init__(self,account, username, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
        

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved contact from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_credentials(cls,account):
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_credentials(cls,account):
        credentials_found = Credentials.find_by_credentials(account)
        pyperclip.copy(credentials_found.credentials) #copy passed in items to the machines clipboard
