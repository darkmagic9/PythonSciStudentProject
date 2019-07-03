import re
import datetime
import validate_email  # sudo pip3 install validate_email

class OperatorValidator:
    """
    This class is called to validate all fields of QLineEdit()-s , before creating 
    and persisting model.Operator.Operator instance into database.
    
    """

    def validateEnrolmentNumber(self, data):
        """
        Validates enrolmentNumber
        
        :param data: string 
        :return: boolean
        """
        try:
            int(data)
        except Exception as err:
            print(err)
            return False

        return True



    def validateFirstName(self, data):
        """
        Validates firstName
        
        :param data: string 
        :return: boolean  
        """
        pattern = r"^[A-Za-z][a-z_]+$"
        ret = re.search(pattern , data)
        if ret:
            return True
        else:
            return False


    def validateLastName(self, data):
        """
        Validates lastName 
        
        :param data: string  
        :return: boolean
        """
        pattern = r"^[A-Za-z][a-z_]+$"
        ret = re.search(pattern , data)
        if ret:
            return True
        else:
            return False


    def validateDob(self, data):
        """
        Validates dob (date of birth)
        
        :param data:  string 
        :return: boolean 
        """
        pattern = r"^19\d{2}-\d{2}-\d{2}$"
        ret = re.search(pattern , data)
        if not(ret): return False


        try:
            values = data.split("-")
            if len(values) != 3: raise Exception("len(values) != 3")
            year = int(values[0])
            month = int(values[1])
            day = int(values[2])
            # that will check bounds for year, month , day automatically
            datetime.date(year, month , day)

        except Exception as err:
            print(err)
            return False


        return True



    def validateFaculty(self, data):
        """
        Validates faculty 
        
        :param data: string  
        :return: boolean 
        """
        pattern = r"^[A-Za-z][a-z_\s]+$"
        ret = re.search(pattern , data)
        if ret:
            return True
        else:
            return False


    def validateEmail(self, data):
        """
        Validates email 
        
        :param data: string  
        :return: boolean 
        """
        isValid = validate_email.validate_email(data)
        return isValid


    def validateId(self, data):
        """
        Validates enrolmentNumber
        
        :param data: string 
        :return: boolean
        """
        try:
            int(data)
        except Exception as err:
            print(err)
            return False

        return True


    def validateCode(self, data):
        """
        Validates enrolmentNumber
        
        :param data: string 
        :return: boolean
        """
        try:
            int(data)
        except Exception as err:
            print(err)
            return False

        return True



    def validateName(self, data):
        """
        Validates faculty 
        
        :param data: string  
        :return: boolean 
        """
        try:
            str(data)
        except Exception as err:
            print(err)
            return False

        return True



    def validateValidation(self, data):
        """
        Validates faculty 
        
        :param data: string  
        :return: boolean 
        """
        try:
            str(data)
        except Exception as err:
            print(err)
            return False

        return True



    def validateRemark(self, data):
        """
        Validates faculty 
        
        :param data: string  
        :return: boolean 
        """
        try:
            str(data)
        except Exception as err:
            print(err)
            return False

        return True

