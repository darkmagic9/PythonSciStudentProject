import datetime


class User:
    def __init__(self,userName="", password=""):
        """
        constructor 
        :param userName: string 
        :param password: string 
        """
        self.userName = userName
        self.password = password

    def __repr__(self):
        """
        This function is called implicitly when repr(), or str() functions are invoked.
        :return: string  
        """
        return "User({0},{1})".format(self.userName, self.password)
    




