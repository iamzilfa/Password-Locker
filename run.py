#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random
import string
import sys

def create_user(username,password):
    """
    Function to create a new user
    """
    new_user = User(username,password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()

def display_user(user):
    """
    Function to display saved user
    """
    return User.display_user()

def login_user(username,password):
    """
    Function that checks whether a user exist and then login the user in.
    """
    check_user = Credential.verify_user(username,password)
    return check_user

def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

def create_credential(account,username,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(account,username,password)
    return new_credential 

def save_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()

def display_credential():
    """
    Function that displays all credentials
    """
    return Credential.display_credential()

def delete_credential(credential):
    """
    Function to delete credentials
    """
    credential.delete_credential()

def find_by_username(username):
    """
    Function that finds in credential a username and returns the credentials that matches that username.
    """
    return Credential.find_by_username(username)



    

