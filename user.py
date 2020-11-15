class User:
    """
    Class that generates new instances of user logins
    """

    user_list = []

    def __init__(self,username,password): 

        """
        initilising user logins
        
        Args:
            username: name of a user
            password: password for a user
        """

        self.username = username
        self.password = password

    def save_user(self):

        """
        Method saves user objects into user_list
        """

        User.user_list.append(self)

   
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        return cls.user_list  
        
