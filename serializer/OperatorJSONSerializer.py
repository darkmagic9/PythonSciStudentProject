import json
from mapper.OperatorJSONMapper import OperatorJSONMapper
class OperatorJSONSerializer:
    """
    This class is used for exporting operators to JSON files, and importing operators 
    from JSON files.

    """
    def exportAsJSON(self, operators):
        """
        Generates JSON data from operators 
        
        :param operators: list of model.Operator.Operator-s
        :return: JSON data 
        """
        ret = None
        l = []
        mapper = OperatorJSONMapper()
        for operator in operators:
            l.append(mapper.map_to_json(operator))
        return json.dumps(l, indent=4, sort_keys=True)


    def exportAsJSONToFile(self, operators , filename = "../files/operators.json"):
        """
        Exports operators to the JSON file with the given filename.

        :param operators: list of model.Operator.Operator-s  
        :param filename: string 
        :return: 
        """
        l = []
        mapper = OperatorJSONMapper()
        for operator in operators:
            l.append(mapper.map_to_json(operator))
        with open(filename, "w") as fh:
            json.dump(l, fh, indent=4, sort_keys=True)



    def importFromJSON(self, filename = "../files/operators.json" ):
        """
        Generates list of model.Operator.Operator-s from JSON file with the given filename.

        :param filename: string 
        :return: list of model.Operator.Operator-s
        """
        operators = []
        mapper = OperatorJSONMapper()
        with open(filename) as fh :
            operators_json = json.load(fh)
            operators = [mapper.map_from_json(data) for data in operators_json]

        return operators