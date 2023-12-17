# DB GUI to manage to database (edit, store and delete)

import tkinter as tk
import logging
import json

from db_datacontainer import DBDataContainer

logging.getLogger().setLevel(logging.INFO)

class StandardQDBEditor(tk.Tk,DBDataContainer):
    
    def __init__(self):
        super().__init__()
        DBDataContainer.__init__(self)
        self.title("JSON Question Database Editor")

        self.entry_widgets = []
        self.load_json_data()
        self.makeform()
        self.q_id = 0

        clear_button = tk.Button(self, text="Clear", command=self.delete_data)
        clear_button.pack(side=tk.RIGHT, padx=10, pady=10)

        update_button = tk.Button(self, text="Update", command=self.update_data)
        update_button.pack(side='left')

        delete_button = tk.Button(self, text="Delete", command=(lambda : self.delete_data(clear_only=False)))
        delete_button.pack(side='left')

        show_button = tk.Button(self, text="Show", command=(lambda : self.show_data(0)))
        show_button.pack(side='left')

        next_button = tk.Button(self, text="Next>", command=(lambda : self.show_data(1)))
        next_button.pack(side='right')

        prev_button = tk.Button(self, text="<Previous", command=(lambda : self.show_data(-1)))
        prev_button.pack(side='right')
    
    def makeform(self):

        # Question ID entry
        lab = tk.Label(self, width=15, text="q_id", anchor='w')
        ent = tk.Entry()
        lab.pack(anchor='w')
        ent.pack(anchor='w')
        self.entry_widgets.append(("q_id", ent))

        # Other question entries
        for field in self.fields.keys():
            lab = tk.Label(self, width=15, text=field, anchor='w')
            if field != "question_text":
                ent = tk.Entry(self, width=30)
            else:
                ent = tk.Text(self, height=10, width=60)
            lab.pack(anchor='w')
            ent.pack(anchor='w')
            self.entry_widgets.append((field, ent))

    def update_data(self):
        
        new_dict = {}
        q_id = 0
        for field,text in self.entry_widgets:
            if field == "q_id" :
                if text.get() != "":
                    self.q_id = int(text.get())
                    text.insert(0, self.q_id)
                else:
                    text.insert(0, len(self.data))
                    q_id = -1
            elif field == "marks" or field == "board":
                new_dict[field] = int(text.get())
            elif field == "question_text":
                new_dict[field] = text.get("1.0", "end-1c")
            else:
                new_dict[field] = text.get()
        if q_id == -1:
            self.data.append(new_dict)
            logging.info("New question {} added".format(len(self.data)))
        else:
            self.data[self.q_id] = new_dict
            logging.info("Question {} update".format(self.q_id+1))
        self.dump_json_data()

    def show_data(self, offset):

        for field,text in self.entry_widgets:
            if field == "q_id" :
                if text.get() != "":
                    self.q_id = int(text.get())
                if (self.q_id + offset) >= 0 and (self.q_id + offset) < len(self.data):
                    self.q_id = self.q_id + offset
                text.delete(0,'end')
                text.insert(0, self.q_id)
            elif field == "question_text":
                text.delete("1.0",tk.END)
                text.insert(tk.END, self.data[self.q_id][field])
            else:
                text.delete(0,'end')
                text.insert(0, self.data[self.q_id][field])

    def delete_data(self,clear_only=True):

        for field,text in self.entry_widgets:
            if field == "q_id" :
                if text.get() != "":
                    self.q_id = int(text.get())
                else:
                    logging.error("Question id invalid")
                    return -1
                text.delete(0,'end')
            elif field == "question_text":
                text.delete("1.0",tk.END)
            else:
                text.delete(0,'end')
        if not clear_only:
            del self.data[self.q_id]
            self.dump_json_data()

class McQDBEditor(tk.Tk,DBDataContainer):
    
    def __init__(self):
        super().__init__()
        DBDataContainer.__init__(self)
        self.title("JSON MCQ Database Editor")

        self.fields = {
                        "marks": 0,
                        "board": 0,
                        "lesson": "",
                        "question_text": "",
                        "options": []
                        }
        self.entry_widgets = []
        self.load_json_data()
        self.makeform()
        self.q_id = 0

        clear_button = tk.Button(self, text="Clear", command=self.delete_data)
        clear_button.pack(side=tk.RIGHT, padx=10, pady=10)

        update_button = tk.Button(self, text="Update", command=self.update_data)
        update_button.pack(side='left')

        delete_button = tk.Button(self, text="Delete", command=(lambda : self.delete_data(clear_only=False)))
        delete_button.pack(side='left')

        show_button = tk.Button(self, text="Show", command=(lambda : self.show_data(0)))
        show_button.pack(side='left')

        next_button = tk.Button(self, text="Next>", command=(lambda : self.show_data(1)))
        next_button.pack(side='right')

        prev_button = tk.Button(self, text="<Previous", command=(lambda : self.show_data(-1)))
        prev_button.pack(side='right')
    
    def makeform(self):

        # Question ID entry
        lab = tk.Label(self, width=15, text="q_id", anchor='w')
        ent = tk.Entry()
        lab.pack(anchor='w')
        ent.pack(anchor='w')
        self.entry_widgets.append(("q_id", ent))

        # Other question entries
        for field in self.fields.keys():                    
            lab = tk.Label(self, width=15, text=field, anchor='w')
            if field != "question_text":
                ent = tk.Entry(self, width=30)
            else:
                ent = tk.Text(self, height=10, width=60)
            lab.pack(anchor='w')
            ent.pack(anchor='w')
            self.entry_widgets.append((field, ent))

    def update_data(self):
        
        new_dict = {}
        q_id = 0
        for field,text in self.entry_widgets:
            if field == "q_id" :
                if text.get() != "":
                    self.q_id = int(text.get())
                    text.insert(0, self.q_id)
                else:
                    text.insert(0, len(self.data))
                    q_id = -1
            elif field == "marks" or field == "board":
                new_dict[field] = int(text.get())
            elif field == "question_text":
                new_dict[field] = text.get("1.0", "end-1c")
            else:
                new_dict[field] = text.get()
        if q_id == -1:
            self.data.append(new_dict)
            logging.info("New question {} added".format(len(self.data)))
        else:
            self.data[self.q_id] = new_dict
            logging.info("Question {} update".format(self.q_id+1))
        self.dump_json_data()

    def show_data(self, offset):

        for field,text in self.entry_widgets:
            if field == "q_id" :
                if text.get() != "":
                    self.q_id = int(text.get())
                if (self.q_id + offset) >= 0 and (self.q_id + offset) < len(self.data):
                    self.q_id = self.q_id + offset
                text.delete(0,'end')
                text.insert(0, self.q_id)
            elif field == "question_text":
                text.delete("1.0",tk.END)
                text.insert(tk.END, self.data[self.q_id][field])
            else:
                text.delete(0,'end')
                text.insert(0, self.data[self.q_id][field])

    def delete_data(self,clear_only=True):

        for field,text in self.entry_widgets:
            if field == "q_id" :
                if text.get() != "":
                    self.q_id = int(text.get())
                else:
                    logging.error("Question id invalid")
                    return -1
                text.delete(0,'end')
            elif field == "question_text":
                text.delete("1.0",tk.END)
            else:
                text.delete(0,'end')
        if not clear_only:
            del self.data[self.q_id]
            self.dump_json_data()