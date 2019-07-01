from dao.StudentDAO import StudentDAO
from pymongo import MongoClient
from mapper.StudentMongoRSMapper import StudentMongoRSMapper

class StudentDAOMongoImpl(StudentDAO):
    """
     This class imlements dao.StudentDAO "interface" . And uses internally pymongo, which
     connects to the mongod database in file

     """

    def __init__(self):
        """
        constructor 
        
        """
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.pymongo_db
        self.mapper = StudentMongoRSMapper()
        self.students = self.db.students


    def drop_collection(self):
        """
        drops collection "students"
        
        :return: 
        """
        try:
            self.students.drop()
        except Exception as err:
            print(str(err))

    def create_collection(self):
        """
        creates collection "students"
        
        :return: 
        """
        self.students = self.db.students

    def save(self, student):
        """
        saves student into collection 
        
        :param student: model.Student.Student  
        :return: 
        """
        self.students.insert_one(self.mapper.map_student_to_dict(student))


    def update(self, enrolmentNumber, student):
        """
        updates old student with enrolmentNumber with new student properties
        
        :param enrolmentNumber: int  
        :param student: model.Student.Student 
        :return: 
        """
        self.students.update_one({"enrolmentNumber": enrolmentNumber}, {
            "$set": {
                "firstName": student.firstName,
                "lastName": student.lastName,
                "dob": str(student.dob),
                "faculty": student.faculty,
                "email": student.email
            }
        })

    def remove(self, enrolmentNumber):
        """
        removes student from colleciton with enrolmentNumber == enrolmentNumber  
        
        :param enrolmentNumber: int  
        :return: 
        """
        self.students.delete_one({"enrolmentNumber": enrolmentNumber})


    def find_by_id(self, enrolmentNumber):
        """
        finds student with enrolmentNumber == enrolmentNumber 
        
        :param enrolmentNumber: int  
        :return:  model.Student.Student 
        """
        props = self.students.find_one({"enrolmentNumber": enrolmentNumber})
        return self.mapper.map_rs_to_student(props)

    def find_all(self):
        """
        finds all students and returns them as a python list 
        
        :return: list of model.Student.Student  
        """
        ret =[]
        for data in self.students.find():
            ret.append(self.mapper.map_rs_to_student(data))

        return ret

