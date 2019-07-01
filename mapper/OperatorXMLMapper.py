from model.Operator import  Operator

class OperatorXMLMapper:
    """
    This class is used by serializer.OperatorXMLSerializer.
    
    """

    def map_from_xml(self, operator_xml):
        """
        creates model.Operator.Operator instance from xml content: operator_xml
        
        :param operator_xml: xml content , which was parsed by Beautifulsoup library
        :return: model.Operator.Operator
        """
        enrolmentNumber = operator_xml.attrs["enrolmentnumber"]
        firstName = operator_xml.find("firstname").contents[0]
        lastName = operator_xml.find("lastname").contents[0]
        dob = operator_xml.find("dob").contents[0]
        faculty = operator_xml.find("faculty").contents[0]
        email = operator_xml.find("email").contents[0]
        return Operator(enrolmentNumber, firstName, lastName, dob , faculty, email)
