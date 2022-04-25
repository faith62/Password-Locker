#!/usr/bin/env python3.9

from password import User, Credentials

def create_user(username, password):
    '''
    Function to create new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()


def create_credentials(account,username,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    function to del credentials
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    function that finds credentials by account and returns the credentials
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    function that check if a credentials exist with that account
    and returns a boolean 
    '''
    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    function that returns all the saved credentialss
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to your credentials list. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New credential")
                print("-"*20)

                print ("Account name:")
                account = input()

                print("Account Username:")
                username = input()

                print("Account Password:")
                password = input()

             
                save_credentials(create_credentials(account, username, password)) # create and save new credentials.
                print ('\n')
                print(f"New Credentials {account} {username} {password} created")
                print ('\n')

        elif short_code == 'dc':

                if display_credentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for account in display_credentials():
                                print(f" Account:{account.account} \n Username:{username} \n Password:{password}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any credentials saved yet")
                        print('\n')

        elif short_code == 'fc':

                print("Enter the Name of the Account you want to search for")

                search_account = input()
                if check_existing_credentials(search_account):
                        search_credentials = find_credentials(search_account)
                        print(f"Account Name: {search_credentials.account}")
                        print('-' * 20)

                        print(f"Username: {search_credentials.username}")
                        print(f"Password: {search_credentials.password}")
                else:
                        print("That account does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()

