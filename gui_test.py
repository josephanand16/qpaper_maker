import tkinter as tk
import json

def update_data():
    with open("data.json") as json_file:
        data = json.load(json_file)
    data["question"] = question_entry.get()
    data["marks"] = marks_entry.get()
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

def show_data():
    with open("data.json") as json_file:
        data = json.load(json_file)
    question_entry.insert(0, data["question"])
    marks_entry.insert(0, data["marks"])

# Create GUI
root = tk.Tk()
root.title("JSON Question Database Editor")

question_label = tk.Label(root, text="Question:")
question_label.pack()

question_entry = tk.Entry(root)
question_entry.pack()

marks_label = tk.Label(root, text="Marks:")
marks_label.pack()

marks_entry = tk.Entry(root)
marks_entry.pack()

update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack(side='left')

show_button = tk.Button(root, text="Show", command=show_data)
show_button.pack(side='right')

# Start GUI main loop
root.mainloop()