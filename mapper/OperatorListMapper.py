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
        operator.dob = str(operator.dob)
        if 'str' not in str(type(operator.dob)):
            dob_str = "-".join([str(operator.dob.year), str(operator.dob.month),
                                str(operator.dob.day)])
        else:
            dob_str = operator.dob


        return [str(operator.enrolmentNumber), operator.firstName, operator.lastName,
                dob_str , operator.faculty, operator.email]


    def map_from_list(self, data):
        """
        create model.Operator.Operator instance from list of strings - data
        :param data: list of strings 
        :return: model.Operator.Operator
        """
        ret = Operator()
        ret.enrolmentNumber =  int(data[0])
        ret.firstName = data[1]
        ret.lastName = data[2]
        ret.dob = datetime.datetime.strptime(data[3], '%Y-%m-%d')
        ret.faculty = data[4]
        ret.email = data[5]
        return ret
