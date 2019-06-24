import csv
from mapper.StudentListMapper import StudentListMapper

class StudentCSVSerializer:
    """
    This class is used for exporting students to CSV files, and importing students 
    from CSV files.
    
    """

    def exportAsCSVToFile(self, students , filename = "files/students.csv"):
        """
        Exports students to the CSV file with the given filename.
        
        :param students: list of model.Student.Student-s  
        :param filename: string 
        :return: 
        """
        with open(filename, "w") as fh:
            writer = csv.writer(fh)
            mapper = StudentListMapper()
            for student in students:
                writer.writerow(mapper.map_to_list(student))




    def importFromCSV(self, filename= "files/students.csv"):
        """
        Generates list of model.Student.Student-s from CSV file with the given filename.
        
        :param filename: string 
        :return: list of model.Student.Student-s
        """
        ret = []
        mapper = StudentListMapper()
        with open(filename) as fh:
            reader = csv.reader(fh)
            for line in reader:
                ret.append(mapper.map_from_list(line))

        return ret