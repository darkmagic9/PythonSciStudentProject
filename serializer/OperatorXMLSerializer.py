from bs4 import BeautifulSoup
from mapper.OperatorXMLMapper import  OperatorXMLMapper
class OperatorXMLSerializer:
    """
    This class is used for exporting operators to XML files, and importing operators 
    from XML files.

    """

    def exportAsXML(self, operators):
        """
        Generates XML data from operators 

        :param operators: list of model.Operator.Operator-s
        :return: XML data 
        """
        ret = """<?xml version = '1.0' encoding = 'UTF-8' ?>
<Operators>
"""
        for operator in operators:
            temp = """<Operator enrolmentNumber = "{0}">
<FirstName>{1}</FirstName>
<LastName>{2}</LastName>
<DOB>{3}</DOB>
<Faculty>{4}</Faculty>
<Email>{5}</Email>
</Operator>
""".format(operator.enrolmentNumber, operator.firstName, operator.lastName,
                    operator.dob, operator.faculty, operator.email)

            ret = ret + temp

        ret += "</Operators>"
        return ret




    def exportAsXMLToFile(self, operators , filename = "files/operators.xml"):
        """
        Exports operators to the XML file with the given filename.

        :param operators: list of model.Operator.Operator-s  
        :param filename: string 
        :return: 
        """
        ret = self.exportAsXML(operators)
        with open(filename, "w") as fh:
            fh.write(ret)



    def importFromXML(self, filename = "files/operators.xml" ):
        """
        Generates list of model.Operator.Operator-s from XML file with the given filename.

        :param filename: string 
        :return: list of model.Operator.Operator-s
        """
        operators = []
        with open(filename) as fh :
            soup = BeautifulSoup(fh , "lxml")
            operators_xml= soup.find_all("operator")
            mapper = OperatorXMLMapper()
            for operator_xml in operators_xml:
                operators.append(mapper.map_from_xml(operator_xml))

        return operators