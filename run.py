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

