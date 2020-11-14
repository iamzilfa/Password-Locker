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

    