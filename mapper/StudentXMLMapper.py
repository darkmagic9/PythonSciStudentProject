from model.Student import  Student

class StudentXMLMapper:
    """
    This class is used by serializer.StudentXMLSerializer.
    
    """

    def map_from_xml(self, student_xml):
        """
        creates model.Student.Student instance from xml content: student_xml
        
        :param student_xml: xml content , which was parsed by Beautifulsoup library
        :return: model.Student.Student
        """
        enrolmentNumber = student_xml.attrs["enrolmentnumber"]
        firstName = student_xml.find("firstname").contents[0]
        lastName = student_xml.find("lastname").contents[0]
        dob = student_xml.find("dob").contents[0]
        faculty = student_xml.find("faculty").contents[0]
        email = student_xml.find("email").contents[0]
        return Student(enrolmentNumber, firstName, lastName, dob , faculty, email)
