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

def copy_passwords(username):
    return Credential.copy_password(username)

def password_locker():
    print("Hello Welcome to you")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do? \n CA....create a new account. \n HA.... Have an account \n")
    short_code = input("").lower().strip()
    if short_code == "CA":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")

        while True:
            print("TP - To type your own password:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = password_Generate()
                break
            else:
                print("Invalid password please try again")
        save_users(create_users(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is:{password}")
        print("*"*85)

    elif short_code == "HA":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_users(username,password)
        if login_users == login:
            print(f"Hello {username}.Welcome To PassWord Locker Generator")
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate a random password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print("TP - To type your own password if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = password_Generate()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_credentials(account,username,password))
            print('\n')
            print(f"Account Credential for: {account} - Username: {username} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_credentials():
                print("Here's your list of accounts: ")

                print('*' * 30)
                print('_'* 30)
                for account in display_credentials():
                    print(f"Account: {account.account} \n User Name:{username}\n Password:{password}")
                    print('_'*30)
                print('*' *30)
            else:
                print("You don't have any credentials saved yet.....")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account Name : {search_credential.username}")
                print('-' * 50)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('/n')
        elif short_code == 'd':
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("-"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for: {search_credential.username} successful deleted")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = password_Generate()
            print(f"{password} Has been generated succesfull/ You can proceedto use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to cintinue")
        



if __name__ == '__main__':
    password_locker()

    



    

