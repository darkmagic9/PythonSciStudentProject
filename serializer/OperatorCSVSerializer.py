import csv
from mapper.OperatorListMapper import OperatorListMapper

class OperatorCSVSerializer:
    """
    This class is used for exporting operators to CSV files, and importing operators 
    from CSV files.
    
    """

    def exportAsCSVToFile(self, operators , filename = "../files/operators.csv"):
        """
        Exports operators to the CSV file with the given filename.
        
        :param operators: list of model.Operator.Operator-s  
        :param filename: string 
        :return: 
        """
        with open(filename, "w") as fh:
            writer = csv.writer(fh)
            mapper = OperatorListMapper()
            for operator in operators:
                writer.writerow(mapper.map_to_list(operator))




    def importFromCSV(self, filename= "../files/operators.csv"):
        """
        Generates list of model.Operator.Operator-s from CSV file with the given filename.
        
        :param filename: string 
        :return: list of model.Operator.Operator-s
        """
        ret = []
        mapper = OperatorListMapper()
        with open(filename) as fh:
            reader = csv.reader(fh)
            for line in reader:
                ret.append(mapper.map_from_list(line))

        return ret