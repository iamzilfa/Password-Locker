class User:
    """
    Class that generates new instances of user logins
    """

    user_list = []

    def __init__(self,username,password): 

        """
        initilising user logins
        """
        self.username = username
        self.password = password

    def save_user(self):

        """
         save_user method saves contact objects into user_list
        """

        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list  

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

   