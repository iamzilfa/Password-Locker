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


