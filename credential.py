#!/usr/bin/env python3.6
import pyperclip
from user import User
import random
import string

class Credential:
    """
    Class that generates new instances of user logins
    """

    credential_list = []

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is our user_list or not
        """
        actual_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                actual_user == user.username
        return actual_user

    def __init__(self,account,username,password): 

        """
        initilising user logins
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):

        """
         save_user method saves contact objects into user_list
        """

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_username(cls,username):

        """
         Method that takes in a username and returns an account that matches that username.
        """

        for credential in cls.credential_list:
            if credential.username == username:
                return credential

    @classmethod
    def copy_password(cls,username):
        credential_found = Credential.find_by_username(username)
        pyperclip.copy(credential_found.password)
                

    @classmethod
    def credential_exist(cls,username):
        '''
         Method that checks if a credential exists from the credential list.
        '''
        for credential in cls.credential_list:
            if credential.username == username:
                return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''

        return cls.credential_list

    