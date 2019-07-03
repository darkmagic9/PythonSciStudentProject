import datetime
from model.Operator import Operator
class OperatorRowMapper:
    """
       This class is used by DAO Implementation classes. 
    """


    def map_from_row(self, row):
        """
        creates model.Operator.Operator instance from list of string-s: row 
        
        :param row: list of string-s  
        :return: model.Operator.Operator
        """
        ret = None
        try:
            id = int(row[0])
            create_date = row[1]
            create_time = row[2]
            # print(row[3])
            create_userfullname = row[3]
            create_userid = row[4]
            update_date = row[5]
            update_time = row[6]
            update_userfullname = row[7]
            update_userid = row[8]
            emp_id = row[9]
            emp_name = row[10]
            is_validator = row[11]
            remark = row[12]
            ret = Operator(id, create_date, create_time, create_userfullname, create_userid, update_date, update_time, update_userfullname, update_userid, emp_id, emp_name, is_validator, remark)
        except Exception as err:
            print(err)

        return ret