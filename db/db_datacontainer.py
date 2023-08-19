class DBDataContainer:
    def __init__(self):
        self._fields = {
            "marks" : 0,
            "board" : False,
            "lesson" : "",
            "question_text" : ""
        }
        self._db_name = "data.json"

    # database Name
    @property
    def db_name(self):
        return self._db_name
    
    @db_name.setter
    def db_name(self, db):
        self._db_name = db

    # fields setter
    @property
    def fields(self):
        return self._fields
    
    @fields.setter
    def fields(self, fld):
        self._fields = fld