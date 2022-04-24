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