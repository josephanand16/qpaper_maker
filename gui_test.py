import tkinter as tk
import logging
import json

logging.getLogger().setLevel(logging.INFO)

def update_data()->int:
    with open("data.json") as json_file:
        data = json.load(json_file)
    getquestion = question_entry.get()
    if getquestion == '':
        logging.error("Question field is empty")
        return -1
    if getquestion not in data.keys():
        data[getquestion] = {}
        logging.info("New question added")
    data[getquestion]["marks"] = marks_entry.get()
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
    return 0

def show_data()->int:
    with open("data.json") as json_file:
        data = json.load(json_file)
    if len(data.keys()) == 0:
        logging.error("Database is empty")
        return -1
    getquestion = question_entry.get()
    if getquestion == '':
        res = list(data.keys())[0]
        question_entry.insert(0, res)
        marks_entry.insert(0, data[res]["marks"])
        logging.info("Showing the first available questions")
    elif len(data.keys()) > 0:
        marks_entry.insert(0, data[getquestion]["marks"])
    return 0

def delete_data():
    with open("data.json") as json_file:
        data = json.load(json_file)
    getquestion = question_entry.get()
    if getquestion in data.keys():
        del data[getquestion]
        question_entry.delete(0,'end')
        marks_entry.delete(0,'end')
    else:
        logging.info("Question not present in database")
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

# Create GUI
root = tk.Tk()
root.title("JSON Question Database Editor")

question_label = tk.Label(root, text="Question:")
question_label.pack()

question_entry = tk.Entry(root, width=50)
question_entry.pack()

marks_label = tk.Label(root, text="Marks:")
marks_label.pack()

marks_entry = tk.Entry(root)
marks_entry.pack()

update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack(side='left')

delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.pack(side='left')

show_button = tk.Button(root, text="Show", command=show_data)
show_button.pack(side='right')

# Start GUI main loop
root.mainloop()