from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer, String, Table, Boolean , Float, BIGINT, DATE
from sqlalchemy.orm import Session , sessionmaker

from dao.OperatorDAO import OperatorDAO


path = "sqlite:///../dbs/OperatorSQlAlchemy.sqlite"
engine = create_engine(path, echo=False)
Base = declarative_base()




class OperatorSQLAlchemy(Base):
    """
    This class extends Base for orm mapping in SQLAlchemy 

    :param enrolmentNumber: long
    :param firstName: string
    :param lastName: string
    :param dob: datetime.date
    :param faculty: string
    :param email: string
    """
    __tablename__ = "OperatorSQLAlchemy"
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
        return "OperatorSQLAlchemy({0}, {1},{2},{3},{4}, {5})".format(
            self.enrolmentNumber, self.firstName, self.lastName,
            self.dob , self.faculty, self.email
        )


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



class OperatorSQLAlchemyDAOImpl(OperatorDAO):
    """
    This class imlements dao.OperatorDAO "interface" . And uses internally sqlite3, which
    connects to the sqlite3 database in file

    """

    def __init__(self):
        """
        constructor 
        
        """
        # clear all instances from table
        for instance in session.query(OperatorSQLAlchemy).order_by(OperatorSQLAlchemy.enrolmentNumber):
            session.delete(instance)


    def save(self, operator):
        """
        saves new model.Operator.Operator instance into database

        :param operator: model.Operator.Operator
        :return: True if save operation was successful, None if save operation failed.
        """
        try:
            session.add(operator)
            session.commit()
        except Exception as err:
            print(err)




    def update(self, enrolmentNumber, operator):
        """
        updates Operator from database with enrolmentNumber == enrolmentNumber

        :param enrolmentNumber: int
        :param operator:  model.Operator.Operator
        :return: 
        """
        try:
            old_operator = session.query(OperatorSQLAlchemy) \
                .filter(OperatorSQLAlchemy.enrolmentNumber == enrolmentNumber).one()

            old_operator.firstName = operator.firstName
            old_operator.lastName = operator.lastName
            old_operator.dob = operator.dob
            old_operator.faculty = operator.faculty
            old_operator.email = operator.email
            session.commit()

        except Exception as err:
            print(err)



    def remove(self, enrolmentNumber):
        """
        removes Operator from database with enrolmentNumber == enrolmentNumber 

        :param enrolmentNumber:int  
        :return: 
        """

        try:
            operator = session.query(OperatorSQLAlchemy)\
                .filter(OperatorSQLAlchemy.enrolmentNumber == enrolmentNumber).one()
            session.delete(operator)
            session.commit()
        except Exception as err:
            print(err)



    def find_by_id(self, enrolmentNumber):
        """
        returns Operator from database with enrolmentNumber == enrolmentNumber or None 
        if no Operator was found in database.

        :param enrolmentNumber: int 
        :return: model.Operator.Operator or None  
        """
        ret = None
        try:
            operator = session.query(OperatorSQLAlchemy)\
                .filter(OperatorSQLAlchemy.enrolmentNumber == enrolmentNumber).one()
            ret = operator
        except Exception as err:
            print(err)

        return ret


    def find_all(self):
        """
        returns all Operator from database, or empty list if table in datbase is empty.

        :return: list() of model.Operator.Operator or empty list
        """
        ret = []
        try:
            ret = session.query(OperatorSQLAlchemy).all()
        except Exception as err:
            print(err)

        return ret



