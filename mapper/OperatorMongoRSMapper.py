from model.Operator import  Operator
import datetime

class OperatorMongoRSMapper:
    """
    This class is used by doa.OperatorDAOMongoImpl.OperatorDAOMongoImpl 
    
    """
    def map_rs_to_operator(self, props):
        """
        maps result set from mongo query into model.Operator.Operator
        
        :param props:  dict of strings 
        :return: model.Operator.Operator 
        """
        dob_str = props["dob"]
        splitted = dob_str.split("-")
        year, month, day = int(splitted[0]), int(splitted[1]), int(splitted[2])
        dob = datetime.date(year, month , day)
        return Operator(int(props["enrolmentNumber"]), props["firstName"],
                       props["lastName"], dob , props["faculty"], props["email"])



    def map_operator_to_dict(self, operator):
        """
        maps model.Operator.Operator into python dict 
        
        :param operator: model.Operator.Operator 
        :return: dict 
        """
        ret = {
            "enrolmentNumber": operator.enrolmentNumber,
            "firstName": operator.firstName,
            "lastName": operator.lastName,
            "dob": str(operator.dob),
            "faculty": operator.faculty,
            "email": operator.email
        }

        return ret