import random as r
from tkinter import *
import sqlite3

count = 0

# sqlite3 stuff

connection = sqlite3.connect('store_names.db')
cursor = connection.cursor()

# create table
command1 = "CREATE TABLE IF NOT EXISTS names(number INTEGER, name TEXT)"
cursor.execute(command1)


# add rows to data
# def put_into_database(iterable_names):
#     count = 1
#     for i in range(len(iterable_names)):
#         command = f"INSERT INTO names VALUES({count}, '{iterable_names[i]}')"
#         cursor.execute(command)
#         count += 1
#     cursor.execute('SELECT * FROM names')
#     return cursor.fetchall()

def get_store():
    name = entry.get()
    entry.delete(0, END)
    into_db(name)


def into_db(name):
    global count
    command = f"INSERT INTO names VALUES({count}, '{name}')"
    cursor.execute(command)
    cursor.execute("SELECT * FROM names")
    print(cursor.fetchall())
    count += 1


# tkinter to test buttons with sql

gui = Tk()
gui.geometry('400x400')

button = Button(gui, text='press', command=get_store)
entry = Entry(gui, font=('Helvetica', 16))

button.pack()
entry.pack()

if __name__ == '__main__':
    first_names = ['sam', 'martha', 'mike', 'yasser', 'branden', 'trevor', 'katherine']
    last_names = ['massnick', 'owens', 'rightnowar', 'alginahi', 'gula', 'trombley', 'berry']

    # full_names = []
    # for i in range(len(first_names)):
    #     first = first_names[r.randint(0, len(first_names) - 1)]
    #     last = last_names[r.randint(0, len(last_names) - 1)]
    #     full_names.append(first + ' ' + last)
    #
    # print(put_into_database(full_names))

    gui.mainloop()
