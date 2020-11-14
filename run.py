#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random
import string
import sys

def create_users(username,password):
    """
    Function to create a new user
    """
    new_user = User(username,password)
    return new_user

def save_users(user):
    """
    Function to save user
    """
    user.save_user()

def display_users(user):
    """
    Function to display saved user
    """
    return User.display_user()

def password_Generate(size = 8, charact=string.ascii_letters + string.digits + string.punctuation):
    """
     Generate a random password using string of letters and digits and special characters
     """
    return''.join(random.choice(charact)for i in range(size))

def login_users(username,password):
    """
    Function that checks whether a user exist and then login the user in.
    """
    check_user = Credential.verify_user(username,password)
    return check_user

def delete_users(user):
    """
    Function to delete a user
    """
    user.delete_user()

def create_credentials(account,username,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(account,username,password)
    return new_credential 

def save_credentials(credential):
    """
    Function to save credential
    """
    credential.save_credential()

def display_credentials():
    """
    Function that displays all credentials
    """
    return Credential.display_credential()

def delete_credentials(credential):
    """
    Function to delete credentials
    """
    credential.delete_credential()

def find_credentials(username):
    """
    Function that finds in credential a username and returns the credentials that matches that username.
    """
    return Credential.find_by_username(username)

def credential_exists(username):
    """
    Function that checks if a credential exists and return true or false.
    """
    return Credential.credential_exist(username)





    

