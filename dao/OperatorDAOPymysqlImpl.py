import pymysql
'''
installing mysqlclient:
 sudo pip3 install mysqlclient
'''
from dao.OperatorDAO import OperatorDAO
from mapper.OperatorRowMapper import OperatorRowMapper

class OperatorDAOPymysqlImpl(OperatorDAO):
    """
    This class imlements dao.OperatorDAO "interface" . And uses internally mysqlclient, which
    connects to the mysql database. 
    It is important to run local mysql server in order to test this class. 
    in ubuntu  , following command launches mysql server: 
    sudo service mysql start
    
    """
    def __init__(self):
        """
        constructor
        """
        self.hostname = "128.100.117.99"
        self.username, self.password = "root", "namiki"
        self.dbname, self.tablename = "lvp-svp", "operator"
        self.db, self.cursor = None, None

    def connect(self):
        """
        connects to the mysql server 
        
        :return: 
        """
        self.db = pymysql.connect(self.hostname, self.username, self.password, self.dbname)
        self.db.autocommit(True)
        self.cursor = self.db.cursor()

    def disconnect(self):
        """
        disconnects from mysql server 
        
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
            # sql = "drop table if exists {0}".format(self.tablename)
            # self.cursor.execute(sql)
            pass
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
            pass
#             sql = """create table if not exists {0} (
# id bigint primary key , 
# create_date varchar(50),
# create_time varchar(50), 
# create_userfullname  date, 
# create_userid varchar(20), 
# update_date, operator.update_time, 
# operator.update_userfullname, operator.update_userid, operator.emp_id, operator.emp_name, operator.is_validator, operator.remark varchar(50)
# )""".format(self.tablename)
#             self.cursor.execute(sql)
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
            sql = """insert into {0} values ({1},"{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}")""".format(
                self.tablename, operator.id, operator.create_date,
                operator.create_time, operator.create_userfullname, operator.create_userid, operator.update_date, operator.update_time, 
                operator.update_userfullname, operator.update_userid, operator.emp_id, operator.emp_name, operator.is_validator, operator.remark
            )

            self.cursor.execute(sql)
        except Exception as err:
            print(err)
            return str(err)
        finally:
            self.disconnect()

        return None



    def update(self, id, operator):
        """
        updates Operator from database with id == id

        :param id: int
        :param operator:  model.Operator.Operator
        :return: 
        """
        self.connect()
        try:
            sql = """update {0} set create_date = "{1}", create_time = "{2}", create_userfullname = "{3}", 
create_userid = "{4}", update_date = "{5}", operator.update_time = "{6}", 
operator.update_userfullname = "{7}", operator.update_userid = "{8}", 
operator.emp_id = "{9}", operator.emp_name = "{10}", operator.is_validator = "{11}", 
operator.remark = "{12}" where id = {13}""".format(
                self.tablename, operator.create_date, operator.create_time, operator.create_userfullname ,
                operator.create_userid , operator.update_date, operator.update_time, 
                operator.update_userfullname, operator.update_userid, operator.emp_id, operator.emp_name, operator.is_validator, operator.remark, id
            )
            self.cursor.execute(sql)
        except Exception as err:
            print(err)

        finally:
            self.disconnect()


    def remove(self, id):
        """
        removes Operator from database with id == id 

        :param id:int  
        :return: 
        """
        self.connect()
        try:
            sql = """delete from {0} where id = {1}""".format(
                self.tablename, id
            )
            self.cursor.execute(sql)
        except Exception as err:
            print(err)
        finally:
            self.disconnect()


    def find_by_id(self, id):
        """
        returns Operator from database with id == id or None 
        if no Operator was found in database.

        :param id: int 
        :return: model.Operator.Operator or None  
        """
        ret = None
        self.connect()
        try:
            sql = """select * from {0} where id = {1}""".format(
               self.tablename, id
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
