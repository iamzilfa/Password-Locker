class Credential:
    """
    Class that generates new instances of user logins
    """

    user_list = []

    def __init__(self,account,username,password): 

        """
        initilising user logins
        """
        self.account = account
        self.username = username
        self.password = password

