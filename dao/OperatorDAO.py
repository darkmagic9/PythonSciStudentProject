class OperatorDAO:
    """
       This class is meant to be an interface , but Python does not have special keyword 
       for interfaces , so the only way is to use "pass" inside every method of this class.
       
    """
    def save(self, operator):
        """
        saves new model.Operator.Operator instance into database
        
        :param operator: model.Operator.Operator
        :return: True if save operation was successful, None if save operation failed.
        """
        pass
    def update(self, enrolmentNumber, operator):
        """
        updates Operator from database with enrolmentNumber == enrolmentNumber
        
        :param enrolmentNumber: int
        :param operator:  model.Operator.Operator
        :return: 
        """
        pass

    def remove(self, enrolmentNumber):
        """
        removes Operator from database with enrolmentNumber == enrolmentNumber 
        
        :param enrolmentNumber:int  
        :return: 
        """
        pass

    def find_by_id(self, enrolmentNumber):
        """
        returns Operator from database with enrolmentNumber == enrolmentNumber or None 
        if no Operator was found in database.
        
        :param enrolmentNumber: int 
        :return: model.Operator.Operator or None  
        """
        pass

    def find_all(self):
        """
        returns all Operator from database, or empty list if table in datbase is empty.
        
        :return: list() of model.Operator.Operator or empty list
        """
        pass