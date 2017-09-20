from dao.StudentDAOSqliteImpl import StudentDAOSqliteImpl
from model.Student import Student
import datetime


class TestStudentDAOSqliteImpl:
    """
    This class was used during development. 
    Tests functionalities of StudentDAOSqliteImpl

    """

    def example1(self):
        """
        
        :return: 
        """
        dao = StudentDAOSqliteImpl()
        dao.drop_table()
        dao.create_table()
        l = [
            Student(1, "foo", "bar", datetime.date(1991, 10, 10), "ai", "foobar@gmail.com"),
            Student(2, "edu", "tilos", datetime.date(1992, 10, 10), "ai", "edutilos@gmail.com"),
            Student(3, "leo", "messi", datetime.date(1993, 10, 10), "ai", "leomessi@gmail.com")
        ]

        for s in l:
            dao.save(s)


        all = dao.find_all()
        print("<<all students>>")
        for s in all:
            print(s)


        # update
        dao.update(1, Student(1, "new_foo", "new_bar", datetime.date(2001, 11, 11), "its", "new_foonewbar@gmail.com"))

        # find one
        one = dao.find_by_id(1)
        print("after update = {0}".format(one))


        # remove one
        dao.remove(1)
        all = dao.find_all()
        print("<<all students after remove by enrolmentNumber = 1>>")
        for s in all:
            print(s)



tester = TestStudentDAOSqliteImpl()
tester.example1()

