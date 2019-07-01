import sqlite3
import sys
print(sys.argv[0])
from dao.OperatorDAO import OperatorDAO
from mapper.OperatorRowMapper import OperatorRowMapper


class OperatorDAOSqliteImpl(OperatorDAO):
    """
    This class imlements dao.OperatorDAO "interface" . And uses internally sqlite3, which
    connects to the sqlite3 database in file
    
    """


    def __init__(self):
        """
        constructor
        
        """
        self.filename = "dbs/Operator.sqlite"
        self.tablename = "Operator"
        self.db, self.cursor = None, None

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
enrolmentNumber bigint primary key , 
firstName varchar(50),
lastName varchar(50), 
dob  date, 
faculty varchar(20), 
email varchar(50)
)""".format(self.tablename)
            self.cursor.execute(sql)
        except Exception as err:
            print(err)

        finally:
            self.disconnect()




    def save(self, operator):
        """
        saves new model.Operator.Operator instance into database

        :param operator: model.Operator.Operator
        :return: True if save operation was successful, None if save operation failed.
        """
        self.connect()
        try:
            sql = """insert into {0} values ({1},"{2}","{3}","{4}","{5}","{6}")""".format(
                self.tablename, operator.enrolmentNumber, operator.firstName,
                operator.lastName, operator.dob, operator.faculty, operator.email
            )

            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print(err)
            return str(err)
        finally:
            self.disconnect()

        return None





    def update(self, enrolmentNumber, operator):
        """
        updates Operator from database with enrolmentNumber == enrolmentNumber

        :param enrolmentNumber: int
        :param operator:  model.Operator.Operator
        :return: 
        """
        self.connect()
        try:
            sql = """update {0} set firstName = "{1}", lastName = "{2}", dob = "{3}", 
faculty = "{4}", email = "{5}" where enrolmentNumber = {6}""".format(
                self.tablename, operator.firstName, operator.lastName, operator.dob ,
                operator.faculty , operator.email, enrolmentNumber
            )
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print(err)

        finally:
            self.disconnect()





    def remove(self, enrolmentNumber):
        """
        removes Operator from database with enrolmentNumber == enrolmentNumber 

        :param enrolmentNumber:int  
        :return: 
        """
        self.connect()
        try:
            sql = """delete from {0} where enrolmentNumber = {1}""".format(
                self.tablename, enrolmentNumber
            )
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print(err)
        finally:
            self.disconnect()





    def find_by_id(self, enrolmentNumber):
        """
        returns Operator from database with enrolmentNumber == enrolmentNumber or None 
        if no Operator was found in database.

        :param enrolmentNumber: int 
        :return: model.Operator.Operator or None  
        """
        ret = None
        self.connect()
        try:
            sql = """select * from {0} where enrolmentNumber = {1}""".format(
               self.tablename, enrolmentNumber
            )
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            ret = OperatorRowMapper().map_from_row(row)
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

        return ret




    def find_all(self):
        """
        returns all Operator from database, or empty list if table in datbase is empty.

        :return: list() of model.Operator.Operator or empty list
        """
        ret = []
        self.connect()
        try:
            sql = """select * from {0}""".format(self.tablename)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            for row in rows:
                ret.append(OperatorRowMapper().map_from_row(row))
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

        return ret
