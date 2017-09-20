import datetime
from model.Student import Student
class StudentRowMapper:
    """
       This class is used by DAO Implementation classes. 
    """


    def map_from_row(self, row):
        """
        creates model.Student.Student instance from list of string-s: row 
        
        :param row: list of string-s  
        :return: model.Student.Student
        """
        ret = None
        try:
            enrolmentNumber = int(row[0])
            firstName = row[1]
            lastName = row[2]
            # print(row[3])
            dob = row[3]
            faculty = row[4]
            email = row[5]
            ret = Student(enrolmentNumber, firstName, lastName, dob , faculty, email)
        except Exception as err:
            print(err)

        return ret