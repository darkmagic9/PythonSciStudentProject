import sys
sys.path.append('.')
from serializer.StudentXMLSerializer import StudentXMLSerializer
from model.Student import  Student
import datetime


class TestStudentXMLSerializer:
    """
    This class was used during development. 
    Tests functionalities of StudentXMLSerializer

    """
    def example1(self):
        """
        
        :return: 
        """
        l = [
            Student(1, "foo", "bar", datetime.date(1991, 10, 10), "ai", "foobar@gmail.com"),
            Student(2, "edu", "tilos", datetime.date(1992, 10, 10), "ai", "edutilos@gmail.com"),
            Student(3, "leo", "messi", datetime.date(1993, 10, 10), "ai", "leomessi@gmail.com")
        ]

        serializer = StudentXMLSerializer()
        serializer.exportAsXMLToFile(l)

        l2 = serializer.importFromXML()
        print("<<all students>>")
        for s in l2:
            print(s)


tester = TestStudentXMLSerializer()
tester.example1()

