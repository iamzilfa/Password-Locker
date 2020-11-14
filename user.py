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

    