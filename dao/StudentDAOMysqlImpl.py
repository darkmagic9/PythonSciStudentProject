import MySQLdb
'''
installing mysqlclient:
 sudo pip3 install mysqlclient
'''
from dao.StudentDAO import StudentDAO
from mapper.StudentRowMapper import StudentRowMapper

class StudentDAOMysqlImpl(StudentDAO):
    """
    This class imlements dao.StudentDAO "interface" . And uses internally mysqlclient, which
    connects to the mysql database. 
    It is important to run local mysql server in order to test this class. 
    in ubuntu  , following command launches mysql server: 
    sudo service mysql start
    
    """
    def __init__(self):
        """
        constructor
        """
        self.hostname = "localhost"
        self.username, self.password = "root", "root"
        self.dbname, self.tablename = "python_sci", "Student"
        self.db, self.cursor = None, None

    def connect(self):
        """
        connects to the mysql server 
        
        :return: 
        """
        self.db = MySQLdb.connect(self.hostname, self.username, self.password, self.dbname)
        self.db.autocommit(on=True)
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

    def save(self, student):
        """
        saves new model.Student.Student instance into database

        :param student: model.Student.Student
        :return: True if save operation was successful, None if save operation failed.
        """
        self.connect()
        try:
            sql = """insert into {0} values ({1},"{2}","{3}","{4}","{5}","{6}")""".format(
                self.tablename, student.enrolmentNumber, student.firstName,
                student.lastName, student.dob, student.faculty, student.email
            )

            self.cursor.execute(sql)
        except Exception as err:
            print(err)
            return str(err)
        finally:
            self.disconnect()

        return None



    def update(self, enrolmentNumber, student):
        """
        updates Student from database with enrolmentNumber == enrolmentNumber

        :param enrolmentNumber: int
        :param student:  model.Student.Student
        :return: 
        """
        self.connect()
        try:
            sql = """update {0} set firstName = "{1}", lastName = "{2}", dob = "{3}", 
faculty = "{4}", email = "{5}" where enrolmentNumber = {6}""".format(
                self.tablename, student.firstName, student.lastName, student.dob ,
                student.faculty , student.email, enrolmentNumber
            )
            self.cursor.execute(sql)
        except Exception as err:
            print(err)

        finally:
            self.disconnect()


    def remove(self, enrolmentNumber):
        """
        removes Student from database with enrolmentNumber == enrolmentNumber 

        :param enrolmentNumber:int  
        :return: 
        """
        self.connect()
        try:
            sql = """delete from {0} where enrolmentNumber = {1}""".format(
                self.tablename, enrolmentNumber
            )
            self.cursor.execute(sql)
        except Exception as err:
            print(err)
        finally:
            self.disconnect()


    def find_by_id(self, enrolmentNumber):
        """
        returns Student from database with enrolmentNumber == enrolmentNumber or None 
        if no Student was found in database.

        :param enrolmentNumber: int 
        :return: model.Student.Student or None  
        """
        ret = None
        self.connect()
        try:
            sql = """select * from {0} where enrolmentNumber = {1}""".format(
               self.tablename, enrolmentNumber
            )
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            ret = StudentRowMapper().map_from_row(row)
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

        return ret

    def find_all(self):
        """
        returns all Student from database, or empty list if table in datbase is empty.

        :return: list() of model.Student.Student or empty list
        """
        ret = []
        self.connect()
        try:
            sql = """select * from {0}""".format(self.tablename)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            for row in rows:
                ret.append(StudentRowMapper().map_from_row(row))
        except Exception as err:
            print(err)
        finally:
            self.disconnect()

        return ret
