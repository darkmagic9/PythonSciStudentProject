from model.Operator import Operator
import datetime

class OperatorListMapper:
    """
    This class is used by serializer.OperatorPDFSerializer.OperatorPDFSerializer and 
    by serializer.OperatorCSVSerializer.OperatorCSVSerializer .

    """

    def map_to_list(self, operator):
        """
        creates list of from model.Operator.Operator
        
        :param operator: model.Operator.Operator
        :return: list of strings 
        """
        operator.create_userfullname = str(operator.create_userfullname)
        if 'str' not in str(type(operator.create_userfullname)):
            create_userfullname_str = "-".join([str(operator.create_userfullname.year), str(operator.create_userfullname.month),
                                str(operator.create_userfullname.day)])
        else:
            create_userfullname_str = operator.create_userfullname


        return [str(operator.id), operator.create_date, operator.create_time,
                create_userfullname_str , operator.create_userid, operator.update_date, 
                operator.update_time, operator.update_userfullname, operator.update_userid, 
                operator.emp_id, operator.emp_name, operator.is_validator, operator.remark]


    def map_from_list(self, data):
        """
        create model.Operator.Operator instance from list of strings - data
        :param data: list of strings 
        :return: model.Operator.Operator
        """
        ret = Operator()
        ret.id =  int(data[0])
        ret.create_date = data[1]
        ret.create_time = data[2]
        # ret.create_userfullname = datetime.datetime.strptime(data[3], '%Y-%m-%d')
        ret.create_userfullname = data[3]
        ret.create_userid = data[4]
        ret.update_date = data[5]
        ret.update_time = data[6]
        ret.update_userfullname = data[7]
        ret.update_userid = data[8]
        ret.emp_id = data[9]
        ret.emp_name = data[10]
        ret.is_validator = data[11]
        ret.remark = data[12]
        return ret
