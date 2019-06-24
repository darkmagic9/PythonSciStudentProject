import sys
sys.path.append('.')
from serializer.StudentCSVSerializer import StudentCSVSerializer
from model.Student import Student

import datetime

class TestStudentCSVSerializer:
    """
    This class was used during development. 
    Tests functionalities of StudentCSVSerializer
    
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

        serializer = StudentCSVSerializer()
        serializer.exportAsCSVToFile(l)

        ret = serializer.importFromCSV()
        print("<<all students>>")
        for student in ret:
            print(student)


tester = TestStudentCSVSerializer()
tester.example1()