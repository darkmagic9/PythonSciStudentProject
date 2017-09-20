from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer, String, Table, Boolean , Float, BIGINT, DATE
from sqlalchemy.orm import Session , sessionmaker

from dao.StudentDAO import StudentDAO


path = "sqlite:///../dbs/StudentSQlAlchemy.sqlite"
engine = create_engine(path, echo=False)
Base = declarative_base()




class StudentSQLAlchemy(Base):
    """
    This class extends Base for orm mapping in SQLAlchemy 

    :param enrolmentNumber: long
    :param firstName: string
    :param lastName: string
    :param dob: datetime.date
    :param faculty: string
    :param email: string
    """
    __tablename__ = "StudentSQLAlchemy"
    enrolmentNumber = Column(BIGINT, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    dob = Column(DATE, nullable=False)
    faculty = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        """
        this method is internally called in python when str() or repr() functions 
        are invpoked. 
        
        :return: string  
        """
        return "StudentSQLAlchemy({0}, {1},{2},{3},{4}, {5})".format(
            self.enrolmentNumber, self.firstName, self.lastName,
            self.dob , self.faculty, self.email
        )


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



class StudentSQLAlchemyDAOImpl(StudentDAO):
    """
    This class imlements dao.StudentDAO "interface" . And uses internally sqlite3, which
    connects to the sqlite3 database in file

    """

    def __init__(self):
        """
        constructor 
        
        """
        # clear all instances from table
        for instance in session.query(StudentSQLAlchemy).order_by(StudentSQLAlchemy.enrolmentNumber):
            session.delete(instance)


    def save(self, student):
        """
        saves new model.Student.Student instance into database

        :param student: model.Student.Student
        :return: True if save operation was successful, None if save operation failed.
        """
        try:
            session.add(student)
            session.commit()
        except Exception as err:
            print(err)




    def update(self, enrolmentNumber, student):
        """
        updates Student from database with enrolmentNumber == enrolmentNumber

        :param enrolmentNumber: int
        :param student:  model.Student.Student
        :return: 
        """
        try:
            old_student = session.query(StudentSQLAlchemy) \
                .filter(StudentSQLAlchemy.enrolmentNumber == enrolmentNumber).one()

            old_student.firstName = student.firstName
            old_student.lastName = student.lastName
            old_student.dob = student.dob
            old_student.faculty = student.faculty
            old_student.email = student.email
            session.commit()

        except Exception as err:
            print(err)



    def remove(self, enrolmentNumber):
        """
        removes Student from database with enrolmentNumber == enrolmentNumber 

        :param enrolmentNumber:int  
        :return: 
        """

        try:
            student = session.query(StudentSQLAlchemy)\
                .filter(StudentSQLAlchemy.enrolmentNumber == enrolmentNumber).one()
            session.delete(student)
            session.commit()
        except Exception as err:
            print(err)



    def find_by_id(self, enrolmentNumber):
        """
        returns Student from database with enrolmentNumber == enrolmentNumber or None 
        if no Student was found in database.

        :param enrolmentNumber: int 
        :return: model.Student.Student or None  
        """
        ret = None
        try:
            student = session.query(StudentSQLAlchemy)\
                .filter(StudentSQLAlchemy.enrolmentNumber == enrolmentNumber).one()
            ret = student
        except Exception as err:
            print(err)

        return ret


    def find_all(self):
        """
        returns all Student from database, or empty list if table in datbase is empty.

        :return: list() of model.Student.Student or empty list
        """
        ret = []
        try:
            ret = session.query(StudentSQLAlchemy).all()
        except Exception as err:
            print(err)

        return ret



