from model.Student import  Student
class StudentJSONMapper:
    """
    This class is used by serializer.StudentJSONSerializer.StudentJSONSerializer
    
    """
    def map_from_json(self, data):
        """
        creates model.Student.Student instance from json map - data
        
        :param data: json map 
        :return: model.Student.Student 
        """
        enrolmentNumber = int(data['enrolmentNumber'])
        firstName = data['firstName']
        lastName = data['lastName']
        dob = data['dob']
        faculty = data['faculty']
        email = data['email']
        return Student(enrolmentNumber, firstName, lastName, dob , faculty, email)

    def map_to_json(self, student):
        """
        creates json map from model.Student.Student - student
        
        :param student: model.Student.Student
        :return: json map 
        """
        ret = {}
        ret['enrolmentNumber'] = student.enrolmentNumber
        ret['firstName'] = student.firstName
        ret['lastName'] = student.lastName
        if 'str' in str(type(student.dob)):
            ret['dob'] = student.dob
        else:
            ret['dob'] = "-".join([str(student.dob.year), str(student.dob.month), str(student.dob.day)])
        ret['faculty'] = student.faculty
        ret['email'] = student.email
        return ret