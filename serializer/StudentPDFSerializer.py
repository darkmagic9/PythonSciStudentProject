from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A2 , A6, A4, A3

from mapper.StudentListMapper import StudentListMapper

class StudentPDFSerializer:
    """
    This class is used for exporting students to PDF files
    
    """

    # table
    def exportAsPDFToFile(self, students , filename="../files/students.pdf"):
        """
        Exports students to the PDF file with the given filename.

        :param students: list of model.Student.Student-s  
        :param filename: string 
        :return: 
        """

        doc = SimpleDocTemplate(filename, pagesize=A3)
        elements = []
        data = []
        data.append(["EnrollmentNumber", "FirstName", "LastName", "DOB",
                     "Faculty", "Email"])
        mapper = StudentListMapper()
        for student in students:
            data.append(mapper.map_to_list(student))

        width = 6
        height = len(data)
        t = Table(data, width * [2 * inch], height * [0.5 * inch])
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
    def exportAsPDFToFile_2(self, students , filename="../files/students.pdf"):
        """
        Exports students to the PDF file with the given filename.

        :param students: list of model.Student.Student-s  
        :param filename: string 
        :return: 
        """

        doc = SimpleDocTemplate(filename)
        styles = getSampleStyleSheet()
        Story = [Spacer(1, 2 * inch)]
        style = styles["Normal"]
        for student in students:
            bogustext = str(student)
            p = Paragraph(bogustext, style)
            Story.append(p)
            Story.append(Spacer(1, 0.2 * inch))
        doc.build(Story)

