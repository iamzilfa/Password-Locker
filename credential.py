class Credential:
    """
    Class that generates new instances of user logins
    """

    credential_list = []

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