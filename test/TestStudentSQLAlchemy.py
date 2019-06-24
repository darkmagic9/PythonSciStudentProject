import sys
sys.path.append('.')
from dao.StudentSQLAlchemy import StudentSQLAlchemy, StudentSQLAlchemyDAOImpl
from model.Student import Student
import datetime


class TestStudentSQLAlchemy:
    """
    This class was used during development. 
    Tests functionalities of StudentSQLAlchemy and StudentSQLAlchemyDAOImpl

    """

    def example1(self):
        """
        
        :return: 
        """
        dao = StudentSQLAlchemyDAOImpl()
        # dao.drop_table()
        # dao.create_table()
        l = [
            StudentSQLAlchemy(enrolmentNumber = 1, firstName = "foo",lastName = "bar",
                              dob = datetime.date(1991, 10, 10), faculty = "ai", email =  "foobar@gmail.com"),
            StudentSQLAlchemy(enrolmentNumber = 2, firstName = "edu", lastName= "tilos",
                              dob = datetime.date(1992, 10, 10), faculty = "ai",email =  "edutilos@gmail.com"),
            StudentSQLAlchemy(enrolmentNumber = 3, firstName = "leo", lastName = "messi",
                              dob = datetime.date(1993, 10, 10), faculty = "ai", email = "leomessi@gmail.com")
        ]

        for s in l:
            dao.save(s)


        all = dao.find_all()
        print("<<all students>>")
        for s in all:
            print(s)


        # update
        dao.update(1, StudentSQLAlchemy(enrolmentNumber = 1, firstName = "new_foo",lastName= "new_bar",
                                        dob = datetime.date(2001, 11, 11), faculty = "its", email = "new_foonewbar@gmail.com"))

        # find one
        one = dao.find_by_id(1)
        print("after update = {0}".format(one))


        # remove one
        dao.remove(1)
        all = dao.find_all()
        print("<<all students after remove by enrolmentNumber = 1>>")
        for s in all:
            print(s)



tester = TestStudentSQLAlchemy()
tester.example1()

