from model.Student import Student
import datetime

class StudentListMapper:
    """
    This class is used by serializer.StudentPDFSerializer.StudentPDFSerializer and 
    by serializer.StudentCSVSerializer.StudentCSVSerializer .

    """

    def map_to_list(self, student):
        """
        creates list of from model.Student.Student
        
        :param student: model.Student.Student
        :return: list of strings 
        """
        student.dob = str(student.dob)
        if 'str' not in str(type(student.dob)):
            dob_str = "-".join([str(student.dob.year), str(student.dob.month),
                                str(student.dob.day)])
        else:
            dob_str = student.dob


        return [str(student.enrolmentNumber), student.firstName, student.lastName,
                dob_str , student.faculty, student.email]


    def map_from_list(self, data):
        """
        create model.Student.Student instance from list of strings - data
        :param data: list of strings 
        :return: model.Student.Student
        """
        ret = Student()
        ret.enrolmentNumber =  int(data[0])
        ret.firstName = data[1]
        ret.lastName = data[2]
        ret.dob = datetime.datetime.strptime(data[3], '%Y-%m-%d')
        ret.faculty = data[4]
        ret.email = data[5]
        return ret
