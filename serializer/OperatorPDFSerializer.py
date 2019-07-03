from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A2 , A6, A4, A3

from mapper.OperatorListMapper import OperatorListMapper

class OperatorPDFSerializer:
    """
    This class is used for exporting operators to PDF files
    
    """

    # table
    def exportAsPDFToFile(self, operators , filename="../files/operators.pdf"):
        """
        Exports operators to the PDF file with the given filename.

        :param operators: list of model.Operator.Operator-s  
        :param filename: string 
        :return: 
        """

        doc = SimpleDocTemplate(filename, pagesize=A3)
        elements = []
        data = []
        data.append(["id", "create_date", "create_time", "create_userfullname",
                     "create_userid", "update_date", "update_time", "update_userfullname",
                     "update_userid", "emp_id", "emp_name", "is_validator", "remark"])
        mapper = OperatorListMapper()
        for operator in operators:
            data.append(mapper.map_to_list(operator))

        width = 13
        height = len(data)
        t = Table(data, width * [1 * inch], height * [0.5 * inch])
        # t.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
        t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.green),
                               ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
                               ]))
        elements.append(t)
        # write the document to disk
        doc.build(elements)


    # This method was never used.But I did not remove this method for learning purposes
    # for myself.
    def exportAsPDFToFile_2(self, operators , filename="../files/operators.pdf"):
        """
        Exports operators to the PDF file with the given filename.

        :param operators: list of model.Operator.Operator-s  
        :param filename: string 
        :return: 
        """

        doc = SimpleDocTemplate(filename)
        styles = getSampleStyleSheet()
        Story = [Spacer(1, 2 * inch)]
        style = styles["Normal"]
        for operator in operators:
            bogustext = str(operator)
            p = Paragraph(bogustext, style)
            Story.append(p)
            Story.append(Spacer(1, 0.2 * inch))
        doc.build(Story)

