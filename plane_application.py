"""
Samuel Massnick, Katherine Berry, Branden Gula
Airplane Priority Queue User Defined Project
"""

from tkinter import *
from plane_button import PlaneButton
from plane_model import *
import sqlite3


plane = Tk()
plane.title('Plane Buttons')

plane.geometry("1200x820")

connection = sqlite3.connect('plane_seating1.db')
cursor = connection.cursor()

personal_priority = IntVar(value=8)  # initializing a variable for the radio buttons with default value 8
plane_mod = PlaneModel()             # initializing the plane model ( priority queue )
count = 0                            # global counting variable to count people who have boarded


def create_tables():
    """ Function to create all needed tables in the database.
        SQL commands are stored in a string and iterated through
        while being executed by the cursor.execute() commands. """
    c_list = ['CREATE TABLE IF NOT EXISTS active_military(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS unattended_minor(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS senior_citizen(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS priority_boarding(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS first_class(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS business_class(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS economy_class(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)',
              'CREATE TABLE IF NOT EXISTS lowest_priority(name TEXT, seat_class TEXT, seat_id TEXT, priority TEXT)']
    for commands in c_list:
        cursor.execute(commands)


def insert_data(name, seat_class, seat_id, priority):
    """ Function that compares priority and stores data using SQL commands.
        Data stored is name, seat class, seat id, and priority. """
    if priority == 1:
        cursor.execute(f"INSERT INTO active_military VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    elif priority == 2:
        cursor.execute(f"INSERT INTO senior_citizen VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    elif priority == 3:
        cursor.execute(f"INSERT INTO unattended_minor VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    elif priority == 4:
        cursor.execute(f"INSERT INTO priority_boarding VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    elif priority == 5:
        cursor.execute(f"INSERT INTO first_class VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    elif priority == 6:
        cursor.execute(f"INSERT INTO business_class VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    elif priority == 7:
        cursor.execute(f"INSERT INTO economy_class VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    else:
        priority = 8
        cursor.execute(f"INSERT INTO lowest_priority VALUES('{name}', '{seat_class}', '{seat_id}', '{Priority(priority)}')")
    connection.commit()  # commit() called to save the database so we can see the changes


def create_flyer(name, priority):
    """ Supplemental function that creates a flyer object
        and returns the flyer to the function call """
    flyer_obj = Flyer(name, Priority(priority))  # creation of the Flyer object
    return flyer_obj


def deselect_radio():
    """ Resets radio buttons by iterating through
        a list of variable names"""
    button_list = [am, um, sc, pqb, fc, bc, ec]
    for buttons in button_list:
        buttons.deselect()


def board_all():
    """ Function that boards all flyers into the plane in their respective order.
        A list of labels is provided to iterate through when the function is called."""
    boarded_list = [boarded1, boarded2, boarded3, boarded4, boarded5, boarded6, boarded7, boarded8, boarded9, boarded10,
                    boarded11, boarded12, boarded13, boarded14, boarded15, boarded16, boarded17, boarded18, boarded19,
                    boarded20, boarded21, boarded22, boarded23, boarded24, boarded25, boarded26, boarded27, boarded28, 
                    boarded29, boarded30]
    if plane_mod.boarding_queue.isEmpty():      # if statement to raise an error if the queue is empty
        response.config(text='Queue Empty')
    else:
        for i in range(len(plane_mod.boarding_queue)):
            boarded_list[i].config(text=f'{plane_mod.boarding_queue.pop()}')  # configs all boarded['text'] variables to contain individual


def claim_seat(button_name):
    """ Function that claims seats for flyers while also
        collecting the information needed. """
    global count        # making sure the func sees the count variable
    if len(name_entry.get()) == 0:      # if the name entry is empty, raise error
        response.config(text='Invalid Entry')
    else:
        if button_name['text'] == 'X':    # if the seat is taken, raise error
            response.config(text='Seat Taken')
        else:
            count += 1                 # incrementing the count variable
            response.config(text='')   # resetting any error codes
            button_name['text'] = 'X'  # claiming seat visually
            button_name.config(background="#ba3045")

            name_storage = name_entry.get()    # grabbing the name and storing it
            name_entry.delete(0, END)  # deleting name after retrieval

            priority_storage = int(personal_priority.get())     # grabbing the priority and storing it
            personal_priority.set(8)        # resetting the priority to the default value

            seat_id = button_name.seat_id       # grabbing and storing seat id
            seat_class = button_name.seat_class # grabbing and storing seat class

            # supplemental function calls
            deselect_radio()
            create_tables()
            insert_data(name_storage, seat_class, seat_id, priority_storage)
            new_flyer = create_flyer(name_storage, priority_storage)
            plane_mod.schedule_flyer(new_flyer)   # call plane mod method to add flyer to priority queue

            if count == 30:         # if plane is full, raise error
                response.config(text='Plane is Full')


def reset():
    """ Reset function to clear the plane and boarding queue.
        It iterates through a list of variable names and resets the
        ['text'] of the labels to an empty string."""
    global count
    count = 0                   # reset count
    plane_mod.__init__()        # reset the boarding queue
    reset_list = [boarded1, boarded2, boarded3, boarded4, boarded5, boarded6, boarded7, boarded8, boarded9, boarded10,
                  boarded11, boarded12, boarded13, boarded14, boarded15, boarded16, boarded17, boarded18, boarded19,
                  boarded20, boarded21, boarded22, boarded23, boarded24, boarded25, boarded26, boarded27, boarded28,
                  boarded29,
                  boarded30, fc1, fc2, fc3, fc4, fc5, fc6, fc7, fc8, fc9, fc10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8,
                  bc9, bc10,
                  ec1, ec2, ec3, ec4, ec5, ec6, ec7, ec8, ec9, ec10, response,]

    for variable in reset_list:
        variable.config(text='')
        if isinstance(variable, PlaneButton):
            variable.config(background="#67bf77")










# name entry
name_entry = Entry(plane, font=('Verdana', 16), bg='#363636', fg='#ffffff', )

# labels
first_class = Label(plane, font=('Verdana', 12, 'bold'), borderwidth=1, relief='solid', text="First Class",
                    bg="#67bf77")
business_class = Label(plane, font=('Verdana', 12, 'bold'), borderwidth=1, relief='solid', text="Business Class",
                       bg="#67bf77")
economy_class = Label(plane, font=('Verdana', 12, 'bold'), borderwidth=1, relief='solid', text="Economy Class",
                      bg="#67bf77")

entry_label = Label(plane, font=('Verdana', 16, 'bold'), borderwidth=1, relief='solid', text="Enter Name", bg="#67bf77")

response_label = Label(plane, font=('Verdana', 16, 'bold'), text="Response", bg="#67bf77", borderwidth=1, relief='solid',)
response = Label(plane, font=('Verdana', 16, 'bold'), text='', width=21, bg="#363636", fg="#ffffff", borderwidth=1, relief='solid',)

priority_label = Label(plane, font=('Verdana', 16, 'bold'), text="Priority", borderwidth=1, relief='solid',
                       bg='#67bf77')

boarded_label = Label(plane, font=('Verdana', 16, 'bold'), text="Boarding Order", borderwidth=1, relief='solid',
                      bg='#67bf77')

# radio buttons
am = Radiobutton(plane, value=1, text='Active Military', bd=1, padx=5, pady=3,
                 font=('Verdana', 12, 'bold'), relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636',
                 tristatevalue='x', variable=personal_priority, )
sc = Radiobutton(plane, value=2, text='Senior Citizen', bd=1, padx=5, pady=3,
                 font=('Verdana', 12, 'bold'), relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636',
                 tristatevalue='x', variable=personal_priority)
um = Radiobutton(plane, value=3, text='Unattended Minor', bd=1, padx=5, pady=3,
                 font=('Verdana', 12, 'bold'), relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636',
                 tristatevalue='x', variable=personal_priority)
pqb = Radiobutton(plane, value=4, text='Priority Queue Boarding', bd=1, padx=5, pady=3,
                  font=('Verdana', 12, 'bold'), relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636',
                  tristatevalue='x', variable=personal_priority)
fc = Radiobutton(plane, value=5, text='First Class', bd=1, padx=5, pady=3, font=('Verdana', 12, 'bold'),
                 relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636', tristatevalue='x',
                 variable=personal_priority)
bc = Radiobutton(plane, value=6, text='Business Class', bd=1, padx=5, pady=3,
                 font=('Verdana', 12, 'bold'), relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636',
                 tristatevalue='x', variable=personal_priority)
ec = Radiobutton(plane, value=7, text='Economy Class', bd=1, padx=5, pady=3, font=('Verdana', 12, 'bold'),
                 relief='solid', bg='#363636', fg='#ffffff', selectcolor='#363636', tristatevalue='x',
                 variable=personal_priority)

# first class
fc1 = PlaneButton(plane, 'first class', 'fc1', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc1))
fc2 = PlaneButton(plane, 'first class', 'fc2', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc2))
fc3 = PlaneButton(plane, 'first class', 'fc3', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc3))
fc4 = PlaneButton(plane, 'first class', 'fc4', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc4))
fc5 = PlaneButton(plane, 'first class', 'fc5', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc5))
fc6 = PlaneButton(plane, 'first class', 'fc6', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc6))
fc7 = PlaneButton(plane, 'first class', 'fc7', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc7))
fc8 = PlaneButton(plane, 'first class', 'fc8', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc8))
fc9 = PlaneButton(plane, 'first class', 'fc9', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground='#48bd5d', command=lambda: claim_seat(fc9))
fc10 = PlaneButton(plane, 'first class', 'fc10', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                   activebackground='#48bd5d', command=lambda: claim_seat(fc10))

# business
bc1 = PlaneButton(plane, 'business class', 'bc1', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc1))
bc2 = PlaneButton(plane, 'business class', 'bc2', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc2))
bc3 = PlaneButton(plane, 'business class', 'bc3', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc3))
bc4 = PlaneButton(plane, 'business class', 'bc4', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc4))
bc5 = PlaneButton(plane, 'business class', 'bc5', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc5))
bc6 = PlaneButton(plane, 'business class', 'bc6', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc6))
bc7 = PlaneButton(plane, 'business class', 'bc7', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc7))
bc8 = PlaneButton(plane, 'business class', 'bc8', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc8))
bc9 = PlaneButton(plane, 'business class', 'bc9', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(bc9))
bc10 = PlaneButton(plane, 'business class', 'bc10', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                   activebackground="#48bd5d", command=lambda: claim_seat(bc10))

# economy
ec1 = PlaneButton(plane, 'economy class', 'ec1', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec1))
ec2 = PlaneButton(plane, 'economy class', 'ec2', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec2))
ec3 = PlaneButton(plane, 'economy class', 'ec3', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec3))
ec4 = PlaneButton(plane, 'economy class', 'ec4', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec4))
ec5 = PlaneButton(plane, 'economy class', 'ec5', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec5))
ec6 = PlaneButton(plane, 'economy class', 'ec6', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec6))
ec7 = PlaneButton(plane, 'economy class', 'ec7', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec7))
ec8 = PlaneButton(plane, 'economy class', 'ec8', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec8))
ec9 = PlaneButton(plane, 'economy class', 'ec9', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                  activebackground="#48bd5d", command=lambda: claim_seat(ec9))
ec10 = PlaneButton(plane, 'economy class', 'ec10', bd=1, padx=5, pady=5, text="", height=1, width=2, bg="#67bf77",
                   activebackground="#48bd5d", command=lambda: claim_seat(ec10))

# function buttons
ba_button = Button(plane, command=board_all, bd=1, padx=5, pady=5, text='Board All', font=('Verdana', 12), bg='#ba3045', activebackground='#b30202' )
reset_button = Button(plane, command=reset, bd=1, padx=5, pady=5, text='Reset', font=('Verdana', 12), bg='#ba3045', activebackground='#b30202' )
quit_button = Button(plane, command=plane.quit, bd=1, padx=5, pady=5, text='X',
                     height=1, width=2, bg='#ba3045', activebackground='#ba3045')

# boarded labels

boarded1 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded2 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded3 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded4 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded5 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded6 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded7 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded8 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded9 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded10 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded11 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded12 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded13 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded14 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded15 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded16 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded17 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded18 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded19 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded20 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded21 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded22 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded23 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded24 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded25 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded26 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded27 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded28 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded29 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")
boarded30 = Label(plane, font=('Verdana', 12, 'bold'), text='', width=30, bg="#363636", fg="#ffffff")

# placing radio buttons
am.place(x=400, y=150)
sc.place(x=400, y=185)
um.place(x=400, y=220)
pqb.place(x=400, y=255)
fc.place(x=400, y=290)
bc.place(x=400, y=325)
ec.place(x=400, y=360)

# entry place
name_entry.place(y=50, x=400)

# placing labels

first_class.place(x=162, y=10)
business_class.place(x=146, y=220)
economy_class.place(x=142, y=430)
entry_label.place(x=400, y=10)

priority_label.place(x=400, y=120)

response_label.place(x=400, y=500)
response.place(x=400, y=530)

# placing seats

fc1.place(x=110, y=50)
fc2.place(x=160, y=50)
fc3.place(x=225, y=50)
fc4.place(x=275, y=50)
fc5.place(x=110, y=100)
fc6.place(x=160, y=100)
fc7.place(x=225, y=100)
fc8.place(x=275, y=100)
fc9.place(x=160, y=150)
fc10.place(x=225, y=150)

bc1.place(x=110, y=260)
bc2.place(x=160, y=260)
bc3.place(x=225, y=260)
bc4.place(x=275, y=260)
bc5.place(x=110, y=310)
bc6.place(x=160, y=310)
bc7.place(x=225, y=310)
bc8.place(x=275, y=310)
bc9.place(x=160, y=360)
bc10.place(x=225, y=360)

ec1.place(x=110, y=470)
ec2.place(x=160, y=470)
ec3.place(x=225, y=470)
ec4.place(x=275, y=470)
ec5.place(x=110, y=520)
ec6.place(x=160, y=520)
ec7.place(x=225, y=520)
ec8.place(x=275, y=520)
ec9.place(x=160, y=570)
ec10.place(x=225, y=570)

ba_button.place(x=400, y=420)
reset_button.place(x=500, y=420)
quit_button.place(x=1150, y=10)

# boarded labels
boarded_label.place(x=800, y=20)
boarded1.place(x=800, y=50)
boarded2.place(x=800, y=75)
boarded3.place(x=800, y=100)
boarded4.place(x=800, y=125)
boarded5.place(x=800, y=150)
boarded6.place(x=800, y=175)
boarded7.place(x=800, y=200)
boarded8.place(x=800, y=225)
boarded9.place(x=800, y=250)
boarded10.place(x=800, y=275)
boarded11.place(x=800, y=300)
boarded12.place(x=800, y=325)
boarded13.place(x=800, y=350)
boarded14.place(x=800, y=375)
boarded15.place(x=800, y=400)
boarded16.place(x=800, y=425)
boarded17.place(x=800, y=450)
boarded18.place(x=800, y=475)
boarded19.place(x=800, y=500)
boarded20.place(x=800, y=525)
boarded21.place(x=800, y=550)
boarded22.place(x=800, y=575)
boarded23.place(x=800, y=600)
boarded24.place(x=800, y=625)
boarded25.place(x=800, y=650)
boarded26.place(x=800, y=675)
boarded27.place(x=800, y=700)
boarded28.place(x=800, y=725)
boarded29.place(x=800, y=750)
boarded30.place(x=800, y=775)

# starting gui

plane.mainloop()
