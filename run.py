#!/usr/bin/env python3.9

from password import Password

def create_password(uname,pwd):
    '''
    Function to create a new password
    '''
    new_password = Password(uname,pwd)
    return new_password

def save_password(password):
    '''
    function to save password
    '''
    password.save_password

def del_password(password):
    '''
    function to del password
    '''
    password.delete_password()

def find_password(user_name):
    '''
    function that finds password by username and returns the password
    '''
    return Password.find_by_user_name(user_name)

def check_existing_password(user_name):
    '''
    function that check if a password exist with that username
    and returns a boolean 
    '''
    return Password.password_exist(user_name)

def display_password():
    '''
    function that returns all the saved passwords
    '''
    return Password.display_password()

def main():
    print("Hello Welcome to your password list. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new password, dc - display passwords, fc -find a password, ex -exit the password list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New password")
                print("-"*10)

                print ("User name ....")
                f_name = input()

                print("Last name ...")
                l_name = input()

                print("Phone number ...")
                p_number = input()

                print("Email address ...")
                e_address = input()


                save_passwords(create_password(f_name,l_name,p_number,e_address)) # create and save new password.
                print ('\n')
                print(f"New password {f_name} {l_name} created")
                print ('\n')

        elif short_code == 'dc':

                if display_passwords():
                        print("Here is a list of all your passwords")
                        print('\n')

                        for password in display_passwords():
                                print(f"{password.first_name} {password.last_name} .....{password.phone_number}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any passwords saved yet")
                        print('\n')

        elif short_code == 'fc':

                print("Enter the number you want to search for")

                search_number = input()
                if check_existing_passwords(search_number):
                        search_password = find_password(search_number)
                        print(f"{search_password.first_name} {search_password.last_name}")
                        print('-' * 20)

                        print(f"Phone number.......{search_password.phone_number}")
                        print(f"Email address.......{search_password.email}")
                else:
                        print("That password does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()

