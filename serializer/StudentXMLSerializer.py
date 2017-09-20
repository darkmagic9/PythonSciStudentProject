from bs4 import BeautifulSoup
from mapper.StudentXMLMapper import  StudentXMLMapper
class StudentXMLSerializer:
    """
    This class is used for exporting students to XML files, and importing students 
    from XML files.

    """

    def exportAsXML(self, students):
        """
        Generates XML data from students 

        :param students: list of model.Student.Student-s
        :return: XML data 
        """
        ret = """<?xml version = '1.0' encoding = 'UTF-8' ?>
<Students>
"""
        for student in students:
            temp = """<Student enrolmentNumber = "{0}">
<FirstName>{1}</FirstName>
<LastName>{2}</LastName>
<DOB>{3}</DOB>
<Faculty>{4}</Faculty>
<Email>{5}</Email>
</Student>
""".format(student.enrolmentNumber, student.firstName, student.lastName,
                    student.dob, student.faculty, student.email)

            ret = ret + temp

        ret += "</Students>"
        return ret




    def exportAsXMLToFile(self, students , filename = "../files/students.xml"):
        """
        Exports students to the XML file with the given filename.

        :param students: list of model.Student.Student-s  
        :param filename: string 
        :return: 
        """
        ret = self.exportAsXML(students)
        with open(filename, "w") as fh:
            fh.write(ret)



    def importFromXML(self, filename = "../files/students.xml" ):
        """
        Generates list of model.Student.Student-s from XML file with the given filename.

        :param filename: string 
        :return: list of model.Student.Student-s
        """
        students = []
        with open(filename) as fh :
            soup = BeautifulSoup(fh , "lxml")
            students_xml= soup.find_all("student")
            mapper = StudentXMLMapper()
            for student_xml in students_xml:
                students.append(mapper.map_from_xml(student_xml))

        return students