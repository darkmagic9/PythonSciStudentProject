import sys
sys.path.append('.')
from dao.OperatorDAOSqliteImpl import OperatorDAOSqliteImpl
from model.Operator import Operator
import datetime


class TestOperatorDAOSqliteImpl:
    """
    This class was used during development. 
    Tests functionalities of OperatorDAOSqliteImpl

    """

    def example1(self):
        """
        
        :return: 
        """
        dao = OperatorDAOSqliteImpl()
        dao.drop_table()
        dao.create_table()
        l = [
            Operator(1, "foo", "bar", datetime.date(1991, 10, 10), "ai", "foobar@gmail.com"),
            Operator(2, "edu", "tilos", datetime.date(1992, 10, 10), "ai", "edutilos@gmail.com"),
            Operator(3, "leo", "messi", datetime.date(1993, 10, 10), "ai", "leomessi@gmail.com")
        ]

        for s in l:
            dao.save(s)


        all = dao.find_all()
        print("<<all operators>>")
        for s in all:
            print(s)


        # update
        dao.update(1, Operator(1, "new_foo", "new_bar", datetime.date(2001, 11, 11), "its", "new_foonewbar@gmail.com"))

        # find one
        one = dao.find_by_id(1)
        print("after update = {0}".format(one))


        # remove one
        dao.remove(1)
        all = dao.find_all()
        print("<<all operators after remove by enrolmentNumber = 1>>")
        for s in all:
            print(s)



tester = TestOperatorDAOSqliteImpl()
tester.example1()

