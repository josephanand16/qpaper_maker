from fpdf import FPDF
from pdf_datacontainer import PdfDataContainer

class QPaper(FPDF,PdfDataContainer):

    def __init__(self, orientation = "portrait", unit = "mm", format = "A4") -> None:

        super().__init__(orientation, unit, format)
        PdfDataContainer.__init__(self)
        self.set_left_margin(4)
        self.total_width = 200

    def header(self):

        self.header_font()
        self.cell(0, self.cw, self.institute, ln=1, align='C')
        self.cell(0, self.cw, self.subject, ln=1, align='C')
        self.sub_header_font()
        self.cell(self.total_width // 3, self.cw, "Date : "+self.date, ln=0, align='L')
        self.header_font()
        self.cell(self.total_width // 3, self.cw, "Class "+str(self.clss), ln=0, align='C')
        self.sub_header_font()
        self.cell(self.total_width // 3 + 5, self.cw, "Marks : "+str(self.marks), ln=0, align='R')
        self.ln(8)
        self.draw_line(0.3)
        self.ln(2)

    def header_font(self):
        self.set_font(self.global_font, 'B', 18)

    def sub_header_font(self):
        self.set_font(self.global_font, 'B', 12)

    def q_header_font(self):
        self.set_font(self.global_font, 'U',10)

    def txt_font(self):
        self.set_font(self.global_font, '', 8)
    
    def draw_line(self,lw):
        self.set_line_width(lw)
        self.line(7, self.get_y(), 205, self.get_y())

    def footer(self):

        self.set_y(-15)
        self.set_font(self.global_font, 'I', 8)
        self.cell(0, 10, '%s' % self.page_no(), 0, 0, 'C')


