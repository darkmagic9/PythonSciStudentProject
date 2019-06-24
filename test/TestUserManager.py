import sys
sys.path.append('.')
from encryption.UserManager import UserManager
from encryption.User import User 
import datetime


class TestUserManager:
    """
    This class was used during development. 
    Tests functionalities of UserManager

    """

    def example1(self):
        """
        
        :return: 
        """
        manager = UserManager()
        manager.drop_table()
        manager.create_table()
        l = [
            User("foo", "bar"),
            User("edu", "tilos"),
            User("leo", "messi")
        ]

        for s in l:
            manager.save(s)


        all = manager.find_all()
        print("<<all users>>")
        for s in all:
            print(s)



        # # update
        # manager.update(User("foo", "bar"), User("new_foo", "new_bar"))
        #
        # # find one
        # one = manager.find_by_userName_and_password(User("new_foo", "new_bar"))
        # print("after update = {0}".format(one))
        #
        #
        # # remove one
        # manager.remove(User("new_foo", "new_bar"))
        #
        #
        # all = manager.find_all()
        # print("<<all users after remove by userName = 'new_foo' and password = 'new_bar'>>")
        # for s in all:
        #     print(s)



tester = TestUserManager()
tester.example1()

