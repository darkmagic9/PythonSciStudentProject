from model.Student import  Student
import datetime

class StudentMongoRSMapper:
    """
    This class is used by doa.StudentDAOMongoImpl.StudentDAOMongoImpl 
    
    """
    def map_rs_to_student(self, props):
        """
        maps result set from mongo query into model.Student.Student
        
        :param props:  dict of strings 
        :return: model.Student.Student 
        """
        dob_str = props["dob"]
        splitted = dob_str.split("-")
        year, month, day = int(splitted[0]), int(splitted[1]), int(splitted[2])
        dob = datetime.date(year, month , day)
        return Student(int(props["enrolmentNumber"]), props["firstName"],
                       props["lastName"], dob , props["faculty"], props["email"])



    def map_student_to_dict(self, student):
        """
        maps model.Student.Student into python dict 
        
        :param student: model.Student.Student 
        :return: dict 
        """
        ret = {
            "enrolmentNumber": student.enrolmentNumber,
            "firstName": student.firstName,
            "lastName": student.lastName,
            "dob": str(student.dob),
            "faculty": student.faculty,
            "email": student.email
        }

        return ret