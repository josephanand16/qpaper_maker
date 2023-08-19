# Class for Getter and setters for pdf parameters

class PdfDataContainer:
    def __init__(self):
        self._global_font = 'Arial'
        self._date = '01.01.1970'
        self._marks = 50
        self._clss = 10
        self._cell_width = 7
        self._institute = "Maxwell Public School"
        self._subject = "Chemistry"

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

# Institution name
    @property
    def institute(self):
        return self._institute
    
    @institute.setter
    def institute(self, inst):
        self._institute = inst

# Subject name
    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, subj):
        self._subject = subj