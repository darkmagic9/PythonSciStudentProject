from serializer.StudentPDFSerializer import StudentPDFSerializer
from model.Student import Student
import datetime


class TestStudentPDFSerializer:
    """
    This class was used during development. 
    Tests functionalities of StudentPDFSerializer

    """

    def example1(self):
        """
        
        :return: 
        """
        serializer = StudentPDFSerializer()
        students = [
            Student(1, "foo", "bar", datetime.date(1991, 10, 10), "ai", "foobar@gmail.com"),
            Student(2, "edu", "tilos", datetime.date(1992, 10, 10), "ai", "edutilos@gmail.com"),
            Student(3, "leo", "messi", datetime.date(1993, 10, 10), "ai", "leomessi@gmail.com")
        ]

        serializer.exportAsPDFToFile(students)


tester = TestStudentPDFSerializer()
tester.example1()