from model.Operator import  Operator
class OperatorJSONMapper:
    """
    This class is used by serializer.OperatorJSONSerializer.OperatorJSONSerializer
    
    """
    def map_from_json(self, data):
        """
        creates model.Operator.Operator instance from json map - data
        
        :param data: json map 
        :return: model.Operator.Operator 
        """
        enrolmentNumber = int(data['enrolmentNumber'])
        firstName = data['firstName']
        lastName = data['lastName']
        dob = data['dob']
        faculty = data['faculty']
        email = data['email']
        return Operator(enrolmentNumber, firstName, lastName, dob , faculty, email)

    def map_to_json(self, operator):
        """
        creates json map from model.Operator.Operator - operator
        
        :param operator: model.Operator.Operator
        :return: json map 
        """
        ret = {}
        ret['enrolmentNumber'] = operator.enrolmentNumber
        ret['firstName'] = operator.firstName
        ret['lastName'] = operator.lastName
        if 'str' in str(type(operator.dob)):
            ret['dob'] = operator.dob
        else:
            ret['dob'] = "-".join([str(operator.dob.year), str(operator.dob.month), str(operator.dob.day)])
        ret['faculty'] = operator.faculty
        ret['email'] = operator.email
        return ret