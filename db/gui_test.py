import tkinter as tk
import logging
import json

from data_container import DBDataContainer

logging.getLogger().setLevel(logging.INFO)

class JsonDBEditor(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("JSON Question Database Editor")
        self.dt = DBDataContainer()
        self.entry_widgets = []
        self.load_json_data()
        self.create_labels_and_entries(self.data)

        update_button = tk.Button(self, text="Update", command=self.update_data)
        update_button.pack(side='left')

        delete_button = tk.Button(self, text="Delete", command=self.delete_data)
        delete_button.pack(side='left')

        show_button = tk.Button(self, text="Show", command=self.show_data)
        show_button.pack(side='right')
    
    def makeform(self):

        for field in self.dt.fields.keys():
            row = tk.Frame(self)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            self.entry_widgets.append((field, ent))

    def create_labels_and_entries(self, data):

        self.marks_label = tk.Label(self, text="Marks:")
        self.marks_label.pack()

        self.marks_entry = tk.Entry(self)
        self.marks_entry.pack()

        self.question_label = tk.Label(self, text="Question:")
        self.question_label.pack()

        self.question_entry = tk.Entry(self, width=50)
        self.question_entry.pack()

    def load_json_data(self):
        with open(self.dt.db_name) as json_file:
            self.data = json.load(json_file)

    def dump_json_data(self):
        with open(self.dt.db_name, "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def update_q_param(self):

        self.data[getquestion]["marks"] = int(self.marks_entry.get())
        self.data[getquestion]["marks"] = int(self.marks_entry.get())

    def update_data(self):

        getquestion = self.question_entry.get()
        if getquestion == '':
            logging.error("Question field is empty")
            return -1
        if getquestion not in self.data.keys():
            self.data[getquestion] = {}
            logging.info("New question added")
        self.data[getquestion]["marks"] = int(self.marks_entry.get())
        self.dump_json_data()
        return 0

    def show_data(self):

        if len(self.data.keys()) == 0:
            logging.error("Database is empty")
            return -1
        getquestion = self.question_entry.get()
        self.marks_entry.delete(0,'end')
        if getquestion == '':
            res = list(self.data.keys())[0]
            self.question_entry.insert(0, res)
            self.marks_entry.insert(0, self.data[res]["marks"])
            logging.info("Showing the first available questions")
        elif len(self.data.keys()) > 0:
            self.marks_entry.insert(0, self.data[getquestion]["marks"])
        return 0

    def delete_data(self):

        getquestion = self.question_entry.get()
        if getquestion in self.data.keys():
            del self.data[getquestion]
            self.question_entry.delete(0,'end')
            self.marks_entry.delete(0,'end')
        else:
            logging.info("Question not present in database")
        self.dump_json_data()

if __name__ == "__main__":
    app = JsonDBEditor()
    app.mainloop()