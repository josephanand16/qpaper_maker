# qpaper - Question paper generator

qpaper\_maker is a tool used to generate question papers based on a database of questions.

The project is subdivided into
 - [ ] Changed from a sqlite database to a json database. It is easier to fill questions.
 - [x] A pdf generator to create a question paper based on the sqlite database.
 - [ ] Requirements changed. PDF creator is redundant. As further editing is not possible. Word seems to be the way.
 - [ ] A word based question paper creator.


19th Aug -
 - Moved the getters and setters to a seperate class
 - Experimenting with Tkinter GUI to read, edit and add questions to the database.
 - Trying to implement the class to be flexible for any type of question database.

17th Dec -
- Will create a Word based question paper creator.
- The questions from the UI will be saved to a json database and then added into a word document.
- Will focus separately on creating a python based word creator.

