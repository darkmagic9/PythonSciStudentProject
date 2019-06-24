import sqlite3
from encryption.UserRowMapper import UserRowMapper
from encryption.Sha256Hasher import Sha256Hasher

class UserManager:
    """
    This class uses internally sqlite3, which connects to the sqlite3 
    database in file

    """

    def __init__(self):
        """
        constructor

        """
        self.filename = "dbs/User.sqlite"
        self.tablename = "User"
        self.db, self.cursor = None, None
        self.hasher = Sha256Hasher()

    def connect(self):
        """
        connects to the sqlite3 server 

        :return: 
        """
        self.db = sqlite3.connect(self.filename)
        # self.db.autocommit(on=True)
        self.cursor = self.db.cursor()

    def disconnect(self):
        """
        disconnects from sqlite3 server 

        :return: 
        """
        if self.db != None:
            self.db.close()

    def drop_table(self):
        """
        drops table with name self.tablename 
        This method has to be used only while testing and debugging 

        :return: 
        """
        self.connect()
        try:
            sql = "drop table if exists {0}".format(self.tablename)
            self.cursor.execute(sql)
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

    def create_table(self):
        """
        creates table with name self.tablename 
        This method has to be used only while testing and debugging 

        :return: 
        """
        self.connect()
        try:
            sql = """create table if not exists {0} (
username varchar(50) not null, 
password varchar(50) not null, 
PRIMARY KEY(username, password)
)""".format(self.tablename)
            self.cursor.execute(sql)
        except Exception as err:
            print(err)

        finally:
            self.disconnect()

    def save(self, user):
        """
        saves new encryption.User.User instance into database

        :param user: encryption.User.User
        :return: True if save operation was successful, None if save operation failed.
        """
        self.connect()
        try:
            sql = """insert into {0} values ("{1}","{2}")""".format(
                self.tablename, user.userName, self.hasher.hash_password(user.password)
            )

            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print(err)
            return str(err)
        finally:
            self.disconnect()

        return None

    def update(self, oldUser, newUser):
        """
        updates encryption.User.User from database with userName == enrolmentNumber

        :param oldUser: encryption.User.User
        :param newUser: encryption.User.User  
        :return: 
        """
        self.connect()
        try:
            sql = """update {0} set userName = "{1}", password = "{2}"
where userName = "{3}" and password = "{4}" """.format(
                self.tablename, newUser.userName, self.hasher.hash_password(newUser.password),
                oldUser.userName, self.hasher.hash_password(oldUser.password)
            )
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print(err)

        finally:
            self.disconnect()

    def remove(self, user):
        """
        removes encryption.User.User from database  

        :param user:encryption.User.User
        :return: 
        """
        self.connect()
        try:
            sql = """delete from {0} where userName = "{1}" and password = "{2}" """.format(
                self.tablename, user.userName, user.password
            )
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print(err)
        finally:
            self.disconnect()


    def find_by_userName_and_password(self, user):
        """
        returns encryption.User.User from database with userName == user.userName and 
        password = user.password 
        or None  if no encryption.User.User was found in database.

        :param user: encryption.User.User
        :return: encryption.User.User or None  
        """
        ret = None
        self.connect()
        try:
            sql = """select * from {0} where userName = "{1}" and password = "{2}" """.format(
                self.tablename, user.userName, user.password
            )
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            ret = UserRowMapper().map_from_row(row)
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

        return ret



    def find_all(self):
        """
        returns all Users from database, or empty list if table in database is empty.

        :return: list() of encryption.User.User or empty list
        """
        ret = []
        self.connect()
        try:
            sql = """select * from {0}""".format(self.tablename)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            for row in rows:
                ret.append(UserRowMapper().map_from_row(row))
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

        return ret
