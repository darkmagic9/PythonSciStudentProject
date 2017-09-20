
from  encryption.User import User


class UserRowMapper:
    """
      This class is used by encryption.UserManager.UserManager
    
    """

    def map_from_row(self, row):
        """
        creates encryption.User.User instance from list of string-s: row 

        :param row: list of string-s  
        :return: encryption.User.User
        """
        ret = None
        try:
            userName = row[0]
            password = row[1]
            return User(userName, password)
        except Exception as err:
            print(err)

        return ret