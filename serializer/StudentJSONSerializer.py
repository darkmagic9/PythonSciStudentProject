import json
from mapper.StudentJSONMapper import StudentJSONMapper
class StudentJSONSerializer:
    """
    This class is used for exporting students to JSON files, and importing students 
    from JSON files.

    """
    def exportAsJSON(self, students):
        """
        Generates JSON data from students 
        
        :param students: list of model.Student.Student-s
        :return: JSON data 
        """
        ret = None
        l = []
        mapper = StudentJSONMapper()
        for student in students:
            l.append(mapper.map_to_json(student))
        return json.dumps(l, indent=4, sort_keys=True)


    def exportAsJSONToFile(self, students , filename = "../files/students.json"):
        """
        Exports students to the JSON file with the given filename.

        :param students: list of model.Student.Student-s  
        :param filename: string 
        :return: 
        """
        l = []
        mapper = StudentJSONMapper()
        for student in students:
            l.append(mapper.map_to_json(student))
        with open(filename, "w") as fh:
            json.dump(l, fh, indent=4, sort_keys=True)



    def importFromJSON(self, filename = "../files/students.json" ):
        """
        Generates list of model.Student.Student-s from JSON file with the given filename.

        :param filename: string 
        :return: list of model.Student.Student-s
        """
        students = []
        mapper = StudentJSONMapper()
        with open(filename) as fh :
            students_json = json.load(fh)
            students = [mapper.map_from_json(data) for data in students_json]

        return students