import datetime
class Operator:
    def __init__(self, id= 0, create_date= "", create_time= "", create_userfullname= "", create_userid = "", update_date= "", update_time= "", update_userfullname= "", update_userid = "", emp_id= "", emp_name= "", is_validator= "", remark = ""):
        """
        constructor 
        
        :param id: long
        :param create_date: string
        :param create_time: string
        :param create_userfullname: string
        :param create_userid: string
        :param update_date: string
        :param update_time: string
        :param update_userfullname: string
        :param update_userid: string
        :param emp_id: string
        :param emp_name: string
        :param is_validator: string
        :param remark: string
        """
        self.id = id
        self.create_date = create_date
        self.create_time = create_time
        self.create_userfullname = create_userfullname
        self.create_userid = create_userid
        self.update_date = update_date
        self.update_time = update_time
        self.update_userfullname = update_userfullname
        self.update_userid = update_userid
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.is_validator = is_validator
        self.remark = remark



    def __repr__(self):
        """
        This function is called implicitly when repr(), or str() functions are invoked.
        :return: string  
        """
        # return "Operator({0},{1}) at faculty {2}".format(self.firstName, self.lastName, self.faculty)
        return "Operator({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{11})".format(
            self.id, self.create_date, self.create_time, self.create_userfullname ,
            self.create_userid, self.update_date, self.update_time, self.update_userfullname, 
            self.update_userid, self.emp_id, self.emp_name, self.is_validator, 
            self.remark
        )




