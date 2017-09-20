class StudentDAO:
    """
       This class is meant to be an interface , but Python does not have special keyword 
       for interfaces , so the only way is to use "pass" inside every method of this class.
       
    """
    def save(self, student):
        """
        saves new model.Student.Student instance into database
        
        :param student: model.Student.Student
        :return: True if save operation was successful, None if save operation failed.
        """
        pass
    def update(self, enrolmentNumber, student):
        """
        updates Student from database with enrolmentNumber == enrolmentNumber
        
        :param enrolmentNumber: int
        :param student:  model.Student.Student
        :return: 
        """
        pass

    def remove(self, enrolmentNumber):
        """
        removes Student from database with enrolmentNumber == enrolmentNumber 
        
        :param enrolmentNumber:int  
        :return: 
        """
        pass

    def find_by_id(self, enrolmentNumber):
        """
        returns Student from database with enrolmentNumber == enrolmentNumber or None 
        if no Student was found in database.
        
        :param enrolmentNumber: int 
        :return: model.Student.Student or None  
        """
        pass

    def find_all(self):
        """
        returns all Student from database, or empty list if table in datbase is empty.
        
        :return: list() of model.Student.Student or empty list
        """
        pass