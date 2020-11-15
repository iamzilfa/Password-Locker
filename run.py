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
    print('='*60)
    print('*' *60)
    print('-' *60)
    print("                   PASSWORD LOCKER")
    print('-' *60)
    print('*' *60)
    print('='*60)
    print("Hello there You're most Welcome")
    print('\n')
    print("-Create New account: CNA\n-Login to your account: LG  \n")
    short_code = input("").lower().strip()
    if short_code == "cna":
        print('\n')
        print("Sign Up")
        print('-' * 30)
        username = input("User_name:")
        print('\n')

        while True:
            print("-Type your password: TP\n-Generate random Password: GP \n")
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
        print('\n')
        print("*"*55)
        print(f"Hello {username}, Your account has been created succesfully!")
        print(f"Your generated password is:{password}")
        print("*"*55)
        print('\n')

    elif short_code == "lg":
        print('\n')
        print("Enter your User name and your Password to log in:")
        print('*'*50)
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
            print(f"Hello {username}. Welcome To PassWord Locker App")
            print('*' * 50)
            print('\n')


    while True:
        print("Use these short codes:")
        print('-'*30)
        print("Create a new credential:    NC\nDisplay Credentials:        DC\nFind a credential:          FC\nDelete credential:          DL\nGenerate a random password: GP\nExit the application:       EX \n")
        short_code = input().lower().strip()


        if short_code == "nc":
            print('\n')
            print("Create New Credential")
            print("-"*20)
            account = input("Account name:")
            username=input("Your username:")
            print('\n')
            while True:
                print("-Type your own password:   YP\n-Generate random Password: GP")
                password_Choice = input().lower().strip()

                if password_Choice == 'yp':
                    password = input("Enter Your Own Password\n")
                    break

                
                elif password_Choice == 'gp':
                    password = password_generates()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_credentials(account,username,password))
            print('\n')
            print(f"Account Credential details:")
            print('*'*50)
            print(f"Account-name: {account}\nUsername: {username}\nPassword:{password}")
            print('*'*50)
            print('\n')
            print(f"{username} what else do you want to do?")
            print('\n')


        elif short_code == "dc":
            print('\n')
            if display_all_credential():
                print("Here's your list of credential accounts: ")
                print('*'* 50)
                for account in display_all_credential():
                    print(f"Account: {account.account} \n Username: {username}\n Password: {password}")
                    print('*'*50)
                    print('\n')
            else:
                print("You don't have any credentials saved yet.....")
                print('\n')


        elif short_code == "fc":
            print()
            print("Enter the username of the Credential you want to search for")
            search_username = input().lower()
            if credential_exists(search_username):
                search_credential = find_credential(search_username)
                print('*' * 50)
                print(f"Account Name : {search_credential.account}")
                print(f"Username: {search_credential.username}")
                print(f"Password :{search_credential.password}")
                print('*' * 50)
                print('\n')
            else:
                print("That Credential does not exist")
                print('\n')


        elif short_code == 'dl':
            print('\n')
            print("Enter the username of the Credential you want to delete")
            search_username = input().lower()
            if credential_exists(search_username):
                search_credential = find_credential(search_username)
                print("*"*50)
                search_credential.delete_credentials()
                print(f"{search_credential.username} stored credentials deleted")
                print('*'*50)
            else:
                print("The Credential does not exist anymore in your store")

        elif short_code == 'gp':

            password = password_generates()
            print('*' *30)
            print(f"{password} Has been succesfull generated\nYou can use it")
            print('*' * 30)
            print('\n')

        elif short_code == 'ex':
            print('\n')
            print('*' * 50)
            print("Thank You for using the App!")
            print('*' * 50)
            print('\n')
            break
        else:
            print("Wrong entry... Try again")
    else:
        print("Please enter a valid input")
        



if __name__ == '__main__':
    main()

    



    

