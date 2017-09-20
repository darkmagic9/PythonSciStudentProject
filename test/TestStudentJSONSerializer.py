from serializer.StudentJSONSerializer import StudentJSONSerializer
from model.Student import  Student
import datetime


class TestStudentJSONSerializer:
    """
    This class was used during development. 
    Tests functionalities of StudentJSONSerializer

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

        serializer = StudentJSONSerializer()
        serializer.exportAsJSONToFile(l)

        l2 = serializer.importFromJSON()
        print("<<all students>>")
        for s in l2:
            print(s)


tester = TestStudentJSONSerializer()
tester.example1()

