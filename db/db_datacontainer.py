# data container class managing the database
import json

class DBDataContainer:
    def __init__(self):
        self._fields = {
            "marks" : 0,
            "board" : 0,
            "lesson" : "",
            "question_text" : ""
        }
        self._db_name = "data/data.json"

    def load_json_data(self):
        with open(self.db_name) as json_file:
            self.data = json.load(json_file)
        if len(self.data) == 0:
            self.data.append(self.fields)
            with open(self.db_name, "w") as json_file:
                json.dump(self.data, json_file, indent=4)

    def dump_json_data(self):
        with open(self.db_name, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

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