from fpdf import FPDF

class QPaper(FPDF):

    def __init__(self, orientation = "portrait", unit = "mm", format = "A4") -> None:

        super().__init__(orientation, unit, format)
        self._global_font = 'Arial'
        self._date = '01.01.1970'
        self._marks = 50
        self._clss = 10
        self._cell_width = 7
        self.set_left_margin(4)
        self.total_width = 200

    def header(self):

        self.header_font()
        self.cell(0, self.cw, "Maxwell Public School", ln=1, align='C')
        self.cell(0, self.cw, "Chemistry", ln=1, align='C')
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

# Getter and setters for 

# Global font
    @property
    def global_font(self):
        return self._global_font

    @global_font.setter
    def global_font(self, font):
        self._global_font = font
    
# Exam date
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, dt):
        self._date = dt

# Question paper marks
    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, mrks):
        self._marks = mrks

# Class Name
    @property
    def clss(self):
        return self._clss
    
    @clss.setter
    def clss(self, cl):
        self._clss = cl

# Cell Width
    @property
    def cw(self):
        return self._cell_width
    
    @cw.setter
    def cw(self, cw):
        self._cell_width = cw
