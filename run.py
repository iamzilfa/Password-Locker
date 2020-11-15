#!/usr/bin/env python3.6
from user import User
from credential import Credential

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

def display_all_credential():
    """
    Function that displays all credentials
    """
    return Credential.display_all_credential()

def password_generates():
    """
    Function that generates a password for the user
    """
    return Credential.password_generate()


def delete_credential(credential):
    """
    Function to delete credentials
    """
    credential.delete_credentials()

def find_credential(username):
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

def main():
    print("Hello There Welcome! \n Please enter you name. \n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
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
                password = password_generates()
                break
            else:
                print("Invalid password please try again")
        save_users(create_users(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is:{password}")
        print("*"*85)

    elif short_code == "li":
        print("*"*5)
        print("Enter your User name and your Password to log in:")
        print('*' * 0)
        username = input("username: ")
        password = input("password: ")
        # login = login_users(username,password)
        if login_users(username,password) == None:
            print('\n')
            print("Please try again")
            print('\n')
        else:
            login_users(username,password)
            print('\n')
            print(f"Hello {username}. Welcome To PassWord Locker Generator")
            print('\n')


    while True:
        print("Use these short codes:\n NC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n D - Delete credential \n GRP - Generate a random password  \n EX - Exit the application \n")
        short_code = input().lower().strip()


        if short_code == "nc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().upper()
            print("Your Account username")
            username = input()
            while True:
                print("YP - To type your own password :\n GRP - Generate random Password")
                password_Choice = input().lower().strip()

                if password_Choice == 'yp':
                    password = input("Enter Your Own Password\n")
                    break

                
                elif password_Choice == 'grp':
                    password = password_generates()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_credentials(account,username,password))
            print('\n')
            print(f"Account Credential for: {account} - Username: {username} - Password:{password} created succesfully")
            print('\n')
            print(f"{username} what else do you want to do?")
            print('\n')


        elif short_code == "dc":
            if display_all_credential():
                print("Here's your list of accounts: ")
                print('_'* 30)

                print('*' * 30)
                for account in display_all_credential():
                    print(f"Account: {account.account} \n Username: {username}\n Password: {password}")
                    print('_'*30)
                print('*' *30)
            else:
                print("You don't have any credentials saved yet.....")


        elif short_code == "fc":
            print("Enter the username of the Credential you want to search for")
            search_username = input().lower()
            if credential_exists(search_username):
                search_credential = find_credential(search_username)
                print(f"Account Name : {search_credential.account}")
                print('-' * 25)
                print('*'* 25)
                print(f"Username: {search_credential.username}")
                print(f"Password :{search_credential.password}")
                print('-' * 25)
                print('*'* 25)
            else:
                print("That Credential does not exist")
                print('/n')


        elif short_code == 'd':
            print("Enter the username of the Credential you want to delete")
            search_username = input().lower()
            if credential_exists(search_username):
                search_credential = find_credential(search_username)
                print("-"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for: {search_credential.username} successful deleted")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'grp':

            password = password_generates()
            print(f"{password} Has been generated succesfull \n You can use it to your account")
            print('\n')

        elif short_code == 'ex':
            print("Thanks for using Password Locker.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")
        



if __name__ == '__main__':
    main()

    



    

