import datetime
class Operator:
    def __init__(self, enrolmentNumber= 0, firstName= "", lastName= "", dob= datetime.date(1991, 10, 10), faculty = "", email= ""):
        """
        constructor 
        
        :param enrolmentNumber: long
        :param firstName: string
        :param lastName: string
        :param dob: datetime.date
        :param faculty: string
        :param email: string
        """
        self.enrolmentNumber = enrolmentNumber
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob
        self.faculty = faculty
        self.email = email



    def __repr__(self):
        """
        This function is called implicitly when repr(), or str() functions are invoked.
        :return: string  
        """
        # return "Operator({0},{1}) at faculty {2}".format(self.firstName, self.lastName, self.faculty)
        return "Operator({0},{1},{2},{3},{4},{5})".format(
            self.enrolmentNumber, self.firstName, self.lastName, self.dob ,
            self.faculty, self.email
        )




